from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse
from django.db.models import Avg, Count
from .models import Teacher, Review, CustomUser, Department, Course, CourseTeacher
from .forms import CustomUserCreationForm

def welcome(request):
    departments = Department.objects.annotate(
        course_count=Count('courses'),
        teacher_count=Count('courses__teacher', distinct=True)
    )
    return render(request, 'welcome.html', {'departments': departments})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Send verification email
            verification_url = request.build_absolute_uri(
                reverse('verify_email', args=[user.verification_token])
            )
            
            html_message = render_to_string('registration/verification_email.html', {
                'user': user,
                'verification_url': verification_url,
            })
            plain_message = strip_tags(html_message)
            
            send_mail(
                'Verify your email address',
                plain_message,
                None,  # Uses DEFAULT_FROM_EMAIL
                [user.email],
                html_message=html_message,
                fail_silently=False,
            )
            
            messages.success(request, 'Registration successful! Please check your email to verify your account.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def verify_email(request, token):
    try:
        user = CustomUser.objects.get(verification_token=token)
        user.is_email_verified = True
        user.save()
        messages.success(request, 'Email verified successfully! You can now log in.')
    except CustomUser.DoesNotExist:
        messages.error(request, 'Invalid verification link.')
    return redirect('login')

@login_required
def department_list(request):
    departments = Department.objects.annotate(
        course_count=Count('courses'),
        teacher_count=Count('courses__teacher', distinct=True)
    ).order_by('code')
    return render(request, 'app/department_list.html', {'departments': departments})

@login_required
def department_detail(request, code):
    department = get_object_or_404(Department, code=code)
    courses = department.courses.annotate(
        teacher_count=Count('teacher', distinct=True),
        avg_rating=Avg('review__rating')
    ).order_by('code')
    return render(request, 'app/department_detail.html', {
        'department': department,
        'courses': courses
    })

@login_required
def course_list(request):
    courses = Course.objects.annotate(
        teacher_count=Count('teacher', distinct=True),
        avg_rating=Avg('review__rating')
    ).order_by('department__code', 'code')
    return render(request, 'app/course_list.html', {'courses': courses})

@login_required
def course_detail(request, code):
    course = get_object_or_404(Course, code=code)
    teachers = Teacher.objects.filter(courses=course).annotate(
        course_rating=Avg('reviews__rating', filter=models.Q(reviews__course=course)),
        overall_rating=Avg('reviews__rating')
    ).order_by('-course_rating')
    return render(request, 'app/course_detail.html', {
        'course': course,
        'teachers': teachers
    })

@login_required
def teacher_list(request):
    department_code = request.GET.get('department')
    course_code = request.GET.get('course')
    
    teachers = Teacher.objects.annotate(
        avg_rating=Avg('reviews__rating'),
        course_count=Count('courses', distinct=True)
    )
    
    if department_code:
        teachers = teachers.filter(courses__department__code=department_code)
    if course_code:
        teachers = teachers.filter(courses__code=course_code)
    
    teachers = teachers.order_by('name')
    
    context = {
        'teachers': teachers,
        'department_code': department_code,
        'course_code': course_code
    }
    return render(request, 'app/teacher_list.html', context)

@login_required
def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    course_id = request.GET.get('course')
    
    reviews = teacher.reviews.all()
    if course_id:
        reviews = reviews.filter(course_id=course_id)
    
    courses = teacher.courses.all()
    course_ratings = []
    for course in courses:
        avg_rating = teacher.reviews.filter(course=course).aggregate(Avg('rating'))['rating__avg']
        course_ratings.append({
            'course': course,
            'avg_rating': avg_rating or 0
        })
    
    return render(request, 'app/teacher_detail.html', {
        'teacher': teacher,
        'reviews': reviews.order_by('-created_at'),
        'course_ratings': course_ratings,
        'current_course_id': course_id
    })

@login_required
def add_review(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    course_id = request.GET.get('course')
    course = None if not course_id else get_object_or_404(Course, id=course_id)
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        course_id = request.POST.get('course')
        
        if course_id:
            course = get_object_or_404(Course, id=course_id)
        
        # Check if user already reviewed this teacher for this course
        review, created = Review.objects.get_or_create(
            teacher=teacher,
            student=request.user,
            course=course,
            defaults={'rating': rating, 'comment': comment}
        )
        
        if not created:
            review.rating = rating
            review.comment = comment
            review.save()
            messages.success(request, 'Your review has been updated!')
        else:
            messages.success(request, 'Your review has been added!')
            
        return redirect('teacher_detail', pk=pk)
    
    # Get courses taught by this teacher
    courses = teacher.courses.all()
    
    return render(request, 'app/add_review.html', {
        'teacher': teacher,
        'courses': courses,
        'selected_course': course
    })

@login_required
def rank_teachers(request):
    department_code = request.GET.get('department')
    course_code = request.GET.get('course')
    
    teachers = Teacher.objects.annotate(
        avg_rating=Avg('reviews__rating'),
        review_count=Count('reviews')
    )
    
    if department_code:
        teachers = teachers.filter(courses__department__code=department_code)
    if course_code:
        teachers = teachers.filter(courses__code=course_code)
        teachers = teachers.annotate(
            course_rating=Avg('reviews__rating', filter=models.Q(reviews__course__code=course_code))
        ).order_by('-course_rating', '-avg_rating', 'name')
    else:
        teachers = teachers.order_by('-avg_rating', 'name')
    
    context = {
        'teachers': teachers,
        'department_code': department_code,
        'course_code': course_code,
        'ranked': True
    }
    return render(request, 'app/teacher_list.html', context)
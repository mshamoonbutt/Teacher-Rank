from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse
from .models import Teacher, Review, CustomUser
from .forms import CustomUserCreationForm
from django.db.models import Avg

def welcome(request):
    return render(request, 'welcome.html')

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
def teacher_list(request):
    teachers = Teacher.objects.annotate(
        avg_rating=Avg('reviews__rating')
    ).order_by('name')
    return render(request, 'app/teacher_list.html', {'teachers': teachers})

@login_required
def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    reviews = teacher.reviews.all().order_by('-created_at')
    return render(request, 'app/teacher_detail.html', {
        'teacher': teacher,
        'reviews': reviews
    })

@login_required
def add_review(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        # Check if user already reviewed this teacher
        review, created = Review.objects.get_or_create(
            teacher=teacher,
            student=request.user,
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
    
    return render(request, 'app/add_review.html', {'teacher': teacher})

@login_required
def rank_teachers(request):
    teachers = Teacher.objects.annotate(
        avg_rating=Avg('reviews__rating')
    ).order_by('-avg_rating', 'name')
    return render(request, 'app/teacher_list.html', {'teachers': teachers, 'ranked': True})

from django.shortcuts import render
from ..models import Teacher, Review
from django.db.models import Avg

def rank_teachers(request):
    teachers = Teacher.objects.annotate(average_rating=Avg('review__rating')).order_by('-average_rating')
    return render(request, 'rank_teachers.html', {'teachers': teachers})
from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('teacher/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('teacher/<int:pk>/review/', views.add_review, name='add_review'),
    path('ranked/', views.rank_teachers, name='rank_teachers'),
] 
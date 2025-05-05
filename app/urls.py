from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/<str:code>/', views.department_detail, name='department_detail'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<str:code>/', views.course_detail, name='course_detail'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('teachers/<int:pk>/review/', views.add_review, name='add_review'),
    path('ranked/', views.rank_teachers, name='rank_teachers'),
] 
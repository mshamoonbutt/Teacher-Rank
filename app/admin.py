from django.contrib import admin
from .models import Teacher, Review

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'email', 'average_rating')
    search_fields = ('name', 'department', 'email')
    list_filter = ('department',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'student', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('teacher__name', 'student__username', 'comment')
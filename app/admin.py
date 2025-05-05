from django.contrib import admin
from .models import Teacher, Review, Department, Course, CourseTeacher

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'created_at')
    search_fields = ('code', 'name', 'description')
    list_filter = ('created_at',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'department', 'credits')
    search_fields = ('code', 'name', 'description', 'department__name')
    list_filter = ('department', 'credits')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'average_rating')
    search_fields = ('name', 'email', 'bio')

@admin.register(CourseTeacher)
class CourseTeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'course', 'semester', 'is_active')
    list_filter = ('semester', 'is_active')
    search_fields = ('teacher__name', 'course__code', 'course__name')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'course', 'student', 'rating', 'created_at')
    list_filter = ('rating', 'created_at', 'course')
    search_fields = ('teacher__name', 'student__username', 'comment', 'course__code')
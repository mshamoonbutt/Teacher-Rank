from django.core.management.base import BaseCommand
from app.models import Department, Course, Teacher, CourseTeacher

class Command(BaseCommand):
    help = 'Check data in the database'

    def handle(self, *args, **options):
        # Check departments
        self.stdout.write('Departments:')
        for dept in Department.objects.all():
            self.stdout.write(f"- {dept.code}: {dept.name}")
        
        # Check teachers
        self.stdout.write('\nTeachers:')
        for teacher in Teacher.objects.all():
            self.stdout.write(f"- {teacher.name} ({teacher.email})")
            if teacher.department:
                self.stdout.write(f"  Department: {teacher.department.name}")
            else:
                self.stdout.write("  Department: None")
        
        # Check courses
        self.stdout.write('\nCourses:')
        for course in Course.objects.all():
            self.stdout.write(f"- {course.code}: {course.name}")
            self.stdout.write(f"  Department: {course.department.name}")
        
        # Check course-teacher relationships
        self.stdout.write('\nCourse-Teacher Relationships:')
        for ct in CourseTeacher.objects.all():
            self.stdout.write(f"- {ct.teacher.name} teaches {ct.course.code} ({ct.semester})") 
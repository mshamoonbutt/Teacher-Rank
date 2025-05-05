from django.core.management.base import BaseCommand
from django.db import transaction
from app.models import Department, Course, Teacher, CourseTeacher
import csv
import os

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        data_dir = 'data'
        
        # Import departments
        self.stdout.write('Importing departments...')
        try:
            with transaction.atomic():
                with open(os.path.join(data_dir, 'departments.csv'), 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        try:
                            department, created = Department.objects.update_or_create(
                                code=row['department_code'].strip(),
                                defaults={
                                    'name': row['department_name'].strip(),
                                    'description': row['description'].strip()
                                }
                            )
                            self.stdout.write(f"{'Created' if created else 'Updated'} department: {department.name}")
                        except Exception as e:
                            self.stdout.write(self.style.ERROR(f"Error importing department {row['department_code']}: {str(e)}"))
                            raise
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing departments: {str(e)}'))
            return
        
        # Print all departments
        self.stdout.write('\nExisting departments:')
        for dept in Department.objects.all():
            self.stdout.write(f"- {dept.code}: {dept.name}")
        
        # Import teachers
        self.stdout.write('\nImporting teachers...')
        try:
            with transaction.atomic():
                with open(os.path.join(data_dir, 'teachers.csv'), 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        try:
                            dept_code = row['department_code'].strip()
                            self.stdout.write(f"Looking for department {dept_code}...")
                            department = Department.objects.get(code=dept_code)
                            self.stdout.write(f"Found department: {department.name}")
                            
                            teacher, created = Teacher.objects.update_or_create(
                                email=row['email'].strip(),
                                defaults={
                                    'name': row['name'].strip(),
                                    'bio': row['bio'].strip(),
                                    'department': department
                                }
                            )
                            self.stdout.write(f"{'Created' if created else 'Updated'} teacher: {teacher.name}")
                        except Department.DoesNotExist:
                            self.stdout.write(self.style.ERROR(f"Department {dept_code} not found for teacher {row['name']}"))
                            raise
                        except Exception as e:
                            self.stdout.write(self.style.ERROR(f"Error importing teacher {row['email']}: {str(e)}"))
                            raise
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing teachers: {str(e)}'))
            return
        
        # Import courses
        self.stdout.write('\nImporting courses...')
        try:
            with transaction.atomic():
                with open(os.path.join(data_dir, 'courses.csv'), 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        try:
                            dept_code = row['department_code'].strip()
                            department = Department.objects.get(code=dept_code)
                            course, created = Course.objects.update_or_create(
                                code=row['course_code'].strip(),
                                defaults={
                                    'name': row['course_name'].strip(),
                                    'department': department,
                                    'credits': int(row['credits'].strip()),
                                    'description': row['description'].strip()
                                }
                            )
                            self.stdout.write(f"{'Created' if created else 'Updated'} course: {course.name}")
                        except Department.DoesNotExist:
                            self.stdout.write(self.style.ERROR(f"Department {dept_code} not found for course {row['course_code']}"))
                            raise
                        except Exception as e:
                            self.stdout.write(self.style.ERROR(f"Error importing course {row['course_code']}: {str(e)}"))
                            raise
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing courses: {str(e)}'))
            return
        
        # Import course-teacher relationships
        self.stdout.write('\nImporting course-teacher relationships...')
        try:
            with transaction.atomic():
                with open(os.path.join(data_dir, 'course_teachers.csv'), 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        try:
                            course = Course.objects.get(code=row['course_code'].strip())
                            teacher = Teacher.objects.get(email=row['teacher_email'].strip())
                            course_teacher, created = CourseTeacher.objects.update_or_create(
                                course=course,
                                teacher=teacher,
                                defaults={
                                    'semester': row['semester'].strip(),
                                    'is_active': row['is_active'].strip().lower() == 'true'
                                }
                            )
                            self.stdout.write(f"{'Created' if created else 'Updated'} course-teacher relationship: {course.code} - {teacher.name}")
                        except Course.DoesNotExist:
                            self.stdout.write(self.style.ERROR(f"Course {row['course_code']} not found for relationship"))
                            raise
                        except Teacher.DoesNotExist:
                            self.stdout.write(self.style.ERROR(f"Teacher {row['teacher_email']} not found for relationship"))
                            raise
                        except Exception as e:
                            self.stdout.write(self.style.ERROR(f"Error importing course-teacher relationship: {str(e)}"))
                            raise
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing course-teacher relationships: {str(e)}'))
            return
        
        self.stdout.write(self.style.SUCCESS('\nSuccessfully imported all data!')) 
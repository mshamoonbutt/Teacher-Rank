from django.test import TestCase
from .models import Teacher

class TeacherModelTest(TestCase):

    def setUp(self):
        Teacher.objects.create(name="John Doe", subject="Math", rating=4.5)

    def test_teacher_creation(self):
        teacher = Teacher.objects.get(name="John Doe")
        self.assertEqual(teacher.subject, "Math")
        self.assertEqual(teacher.rating, 4.5)
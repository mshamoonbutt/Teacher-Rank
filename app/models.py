from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name
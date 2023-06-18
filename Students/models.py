from django.db import models

# Create your models here.
# Students/models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

class Progress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    progress = models.FloatField()  # Represent progress as a percentage

class AppUsage(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    last_used = models.DateTimeField()  # Store the last time the app was used

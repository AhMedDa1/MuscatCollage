from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)

    def progress(self):
        progress_record = Progress.objects.filter(student=self).first()
        return progress_record.progress if progress_record else None

    def last_app_usage(self):
        app_usage_record = AppUsage.objects.filter(student=self).first()
        return app_usage_record.last_used if app_usage_record else None

class Progress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    progress = models.FloatField()  # Represent progress as a percentage

class AppUsage(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    last_used = models.DateTimeField()  # Store the last time the app was used

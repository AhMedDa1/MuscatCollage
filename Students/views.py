from django.shortcuts import render
from .models import Student, Progress, AppUsage

def dashboard(request):
    students = Student.objects.all()
    progress = Progress.objects.all()
    app_usage = AppUsage.objects.all()

    context = {
        'students': students,
        'progress': progress,
        'app_usage': app_usage,
    }

    return render(request, 'dashboard.html', context)

from rest_framework import viewsets
from .models import Student, Progress, AppUsage
from .serializers import StudentSerializer, ProgressSerializer, AppUsageSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

class AppUsageViewSet(viewsets.ModelViewSet):
    queryset = AppUsage.objects.all()
    serializer_class = AppUsageSerializer
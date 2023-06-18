from rest_framework import serializers
from .models import Student, Progress, AppUsage

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'

class AppUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUsage
        fields = '__all__'
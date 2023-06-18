from django.contrib import admin
from .models import Student, Progress, AppUsage

class ProgressInline(admin.StackedInline):
    model = Progress
    extra = 1  # number of extra forms

class AppUsageInline(admin.StackedInline):
    model = AppUsage
    extra = 1  # number of extra forms

class StudentAdmin(admin.ModelAdmin):
    inlines = [ProgressInline, AppUsageInline]

admin.site.register(Student, StudentAdmin)

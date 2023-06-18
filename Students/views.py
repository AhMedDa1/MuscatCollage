from django.shortcuts import render, redirect
from .models import Student, Progress, AppUsage
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app


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


from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials, firestore



def my_view(request):
    # Use the application default credentials
    cred = credentials.Certificate('bewell.json')

    # Initialize the Firebase app if not already initialized
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)

    # Access the Firestore client
    db = firestore.client()

    # Retrieve student document data
    student_doc_ref = db.collection('progress').document('8a1la2MLXpTYy9Kt6H9a')
    student_doc = student_doc_ref.get().to_dict()

    # Retrieve values from the student document
    student_name = student_doc.get('studentName')
    last_using = student_doc.get('lastUsing')
    progress = student_doc.get('progress')

    # Pass the retrieved values to the template context
    context = {
        'student_name': student_name,
        'last_using': last_using,
        'progress': progress,
    }

    return render(request, 'bewell.html', context)



# def my_view(request):
#     # Use the application default credentials
#     cred = credentials.Certificate('bewell.json')

#     try:
#         firebase_admin.get_app()
#     except ValueError as e:
#         firebase_admin.initialize_app(cred)

#     db = firestore.client()

#     # Retrieving document data
#     doc_ref = db.collection('course').document('oMCKo18PFKw9xGnk1N6x')
#     doc = doc_ref.get().to_dict()

#     # Retrieving values
#     course_image = doc.get('courseImage')
#     course_name = doc.get('courseName')
#     lessons = doc.get('lessons')

#     # Pass the retrieved values to the template context
#     context = {
#         'course_image': course_image,
#         'course_name': course_name,
#         'lessons': lessons,
#     }

#     return render(request, 'bewell.html', context)



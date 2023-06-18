from django.urls import path
from .views import dashboard
# from .views import students_view
from .views import my_view 

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    # path('students/', students_view, name='students'),
    path('my_view/', my_view, name='my_view'),
   
]
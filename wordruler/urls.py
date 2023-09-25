from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='wordruler'),
    path('students', views.wr_students, name='wordruler_students'),
    path('<int:student_id>', views.wr_student, name='wordruler_student'),
]
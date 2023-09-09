from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='students'),
    path('<int:student_id>', views.student, name='student')
]
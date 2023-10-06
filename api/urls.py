from django.urls import path
from . import views

urlpatterns = [
    path('letters/add/', views.LetterAPIView.as_view()),
    path('letters/list/', views.ListLetters.as_view()),
    path('letters/<int:pk>/', views.letter_detail),

    path('wordrulers/add/', views.WordRulerAPIView.as_view()),
    path('wordrulers/list/', views.WordRulerAPIView.as_view()),
    path('wordrulers/<int:pk>/', views.WordRulerAPIView.as_view()),

    path('students/add/', views.ListStudents.as_view()),
    path('students/list/', views.ListStudents.as_view()),
    path('students/<int:pk>/', views.ListStudents.as_view()),

    path('teachers/add/', views.ListStudents.as_view()),
    path('teachers/list/', views.ListStudents.as_view()),
    path('teachers/<int:pk>/', views.ListStudents.as_view()),
    
    path('lessons/add/', views.ListStudents.as_view()),
    path('lessons/list/', views.ListLessons.as_view()),
    path('lessons/by_student/<int:student_pk>/', views.lesson_get_by_student),

    path('util/get_student_letters/', views.create_letter_dict_by_student),
]
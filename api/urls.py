from django.urls import path
from . import views

urlpatterns = [
    path('addletter/', views.LetterAPIView.as_view()),
    path('addwr/', views.WordRulerAPIView.as_view()),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='teachers'),
    path('<int:teacher_id>', views.teacher, name='teacher')
]
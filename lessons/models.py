from django.db import models
from students.models import Student
from teachers.models import Teacher

class Lesson(models.Model):
    lesson_title = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lesson_date = models.DateField(auto_now_add=True)
    content = models.TextField()
    recurring = models.BooleanField()

    def __str__(self):
        return str(self.lesson_title)
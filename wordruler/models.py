from django.db import models
from students.models import Student
from teachers.models import Teacher


class Letter(models.Model):
    letter = models.CharField(max_length=1)
    letter_name = models.CharField(max_length=200)
    letter_img = models.ImageField(upload_to='photos/letters/', blank=True)

    class Meta:
        ordering = ["letter"]

    def __str__(self):
        return str(self.letter_name)


class Wordruler(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    letters = models.ManyToManyField(Letter, blank=True)

    def __str__(self):
        return str(f"{self.teacher.name}_{self.student.name}")



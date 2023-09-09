from django.db import models
from students.models import Student

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=f'photos/teachers/{name}/', blank=True)

    def __str__(self):
        return str(self.name)
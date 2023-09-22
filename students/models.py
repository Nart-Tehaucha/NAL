from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/students/', default='./photos/students/photo_placeholder.jpg')

    def __str__(self):
        return str(self.name)

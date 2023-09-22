from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/teachers/', default='./photos/teachers/photo_placeholder.jpg')

    def __str__(self):
        return str(self.name)
# Generated by Django 4.2.4 on 2023-09-09 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(default='./photos/students/photo_placeholder.jpg', upload_to='photos/students/'),
        ),
    ]

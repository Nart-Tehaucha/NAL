# Generated by Django 4.2.4 on 2023-09-23 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0005_alter_teacher_photo'),
        ('students', '0005_alter_student_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=1)),
                ('letter_name', models.CharField(max_length=200)),
                ('letter_img', models.ImageField(default='./photos/students/photo_placeholder.jpg', upload_to='photos/letters/')),
            ],
        ),
        migrations.CreateModel(
            name='Wordruler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letters', models.ManyToManyField(to='wordruler.letter')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
        ),
    ]

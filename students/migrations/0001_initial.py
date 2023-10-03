# Generated by Django 4.2.4 on 2023-10-03 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('photo', models.ImageField(default='./photos/students/photo_placeholder.jpg', upload_to='photos/students/')),
            ],
        ),
    ]

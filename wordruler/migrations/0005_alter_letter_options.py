# Generated by Django 4.2.4 on 2023-09-23 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordruler', '0004_alter_letter_letter_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='letter',
            options={'ordering': ['letter']},
        ),
    ]

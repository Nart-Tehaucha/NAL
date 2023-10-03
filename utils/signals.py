from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import django.contrib.auth as django_contrib_auth

@receiver(post_save, sender=django_contrib_auth.get_user_model(), weak=False)
def report_uploaded(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
from django.apps import AppConfig


class WordrulerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wordruler'

    def ready(self):
        import utils.signals

from django.apps import AppConfig


class QrauthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'qrauth'

    def ready(self):
        import qrauth.signals

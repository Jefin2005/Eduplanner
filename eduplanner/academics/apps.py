from django.apps import AppConfig

class AcademicsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'academics'

    def ready(self):
        from .utils import setup_initial_data
        setup_initial_data()

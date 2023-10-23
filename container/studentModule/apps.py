from django.apps import AppConfig


class StudentmoduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'studentModule'
    def ready(self):
        import studentModule.signals

from django.apps import AppConfig


# class CoreConfig(AppConfig):
#     name = 'core'

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' 
    name = 'mysite.core'

    def ready(self):
        from jobs import updater
        updater.start()
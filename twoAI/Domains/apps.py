from django.apps import AppConfig


class DomainsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Domains'

    def ready(self):
        import Domains.signals 

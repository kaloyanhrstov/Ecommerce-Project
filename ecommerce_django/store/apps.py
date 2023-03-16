from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce_django.store'

    def ready(self):
        pass

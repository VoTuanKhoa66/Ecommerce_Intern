from django.apps import AppConfig


class OrderDetailsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order_details'

    def ready(self):
        import order_details.signals

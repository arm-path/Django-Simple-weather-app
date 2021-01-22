from django.apps import AppConfig


class ApplicationConfig(AppConfig):
    name = 'application'

    class Meta:
        verbose_name = 'Weather Django'
        verbose_name_plural = 'Weathers Django'

from django.apps import AppConfig

from App2.settings import DEFAULT_AUTO_FIELD


class DespesaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.despesa'

from django.apps import AppConfig

from App2.settings import DEFAULT_AUTO_FIELD
class AnimalConfig(AppConfig):
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    name = 'apps.animal'



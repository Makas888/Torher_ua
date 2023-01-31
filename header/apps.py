from django.apps import AppConfig
import os
from django.conf import settings


class HeaderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'header'
    path = os.path.join(settings.BASE_DIR, 'header')

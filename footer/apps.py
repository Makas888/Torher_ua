from django.apps import AppConfig
import os
from django.conf import settings


class FooterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'footer'
    path = os.path.join(settings.BASE_DIR, 'footer')


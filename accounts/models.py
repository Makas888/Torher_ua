from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Чоловіча'),
        ('f', 'Жіноча'),
    )
    gender = models.CharField('Стать', max_length=1, choices=GENDERS, default='m')
    phone = models.CharField('Телефон', max_length=25)

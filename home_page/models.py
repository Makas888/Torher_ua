from django.db import models
from uuid import uuid4
import os

from django.db.models.signals import pre_delete
from django.dispatch import receiver


class HeroSection(models.Model):
    """slides with a description on the start page"""

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/slides', f'{uuid4()}.{ext}')

    title = models.CharField('Заголовок', max_length=50, unique=True)
    desc = models.TextField('Опис', max_length=300)
    photo = models.ImageField('Фото', upload_to=get_file_name)
    is_visible = models.BooleanField('Відображення', default=True)

    class Meta:
        verbose_name = 'слайди у шапці'
        verbose_name_plural = 'слайди у шапці'

    def __str__(self):
        return f'{self.title}'


class News(models.Model):
    """sales information on the start page"""

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/block_news', f'{uuid4()}.{ext}')

    title = models.CharField('Заголовок', max_length=25)
    description = models.CharField('Опис', max_length=500)
    image = models.ImageField('Зображення', upload_to=get_file_name)

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'

    def __str__(self):
        return f'{self.title} - {self.description[:25]}'


class NewsVisible(models.Model):
    """sales position on the start page"""

    left_block = models.ForeignKey(News,
                                   verbose_name='Лівий блок',
                                   on_delete=models.CASCADE,
                                   related_name='left_block')
    right_block = models.ForeignKey(News,
                                    verbose_name='Правий блок',
                                    on_delete=models.CASCADE,
                                    related_name='right_block')
    is_visible = models.BooleanField('Відобразити', unique=True)

    class Meta:
        verbose_name = 'Відображення новин'
        verbose_name_plural = 'Відображення новин'
        ordering = ('-is_visible', )

    def __str__(self):
        return 'Активне' if self.is_visible else 'Неактивне'


@receiver(pre_delete, sender=News)
def image_News_delete(instance, **kwargs):
    """Deletes files in the "media" folder after deleting the News object"""

    if instance.image:
        instance.image.delete(False)


@receiver(pre_delete, sender=HeroSection)
def photo_HeroSection_delete(instance, **kwargs):
    """Deletes files in the "media" folder after deleting the HeroSection object"""

    if instance.photo:
        instance.photo.delete(False)

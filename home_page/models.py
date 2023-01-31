from django.db import models
from uuid import uuid4
import os


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


class SeasonSale(models.Model):
    """sales information on the start page"""

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/slides', f'{uuid4()}.{ext}')

    information = models.CharField('Загальна інформація', max_length=50)
    max_discount = models.PositiveSmallIntegerField('Максимальна знижка')
    image = models.ImageField('Зображення', upload_to=get_file_name)

    class Meta:
        verbose_name = 'Pозпродаж'
        verbose_name_plural = 'Pозпродаж'

    def __str__(self):
        return f'{self.information} - {self.max_discount}'


class SeasonSaleVisible(models.Model):
    """sales position on the start page"""

    left_block = models.ForeignKey(SeasonSale,
                                   verbose_name='Лівий блок',
                                   on_delete=models.DO_NOTHING,
                                   related_name='left_block')
    right_block = models.ForeignKey(SeasonSale,
                                    verbose_name='Правий блок',
                                    on_delete=models.DO_NOTHING,
                                    related_name='right_block')
    is_visible = models.BooleanField('Відобразити', unique=True)

    class Meta:
        verbose_name = 'Відображення розпродажу'
        verbose_name_plural = 'Відображення розпродажу'
        ordering = ('-is_visible', )

    def __str__(self):
        return 'Активне' if self.is_visible else 'Неактивне'

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class SubjectCoupons(models.Model):
    name = models.CharField('Назва тематики', max_length=30)

    class Meta:
        verbose_name = 'Тематки купона'
        verbose_name_plural = 'Тематики купонів'

    def __str__(self):
        return self.name


class Coupon(models.Model):
    subject = models.ForeignKey(SubjectCoupons, verbose_name='Тематика купону', on_delete=models.CASCADE)
    code = models.CharField('унікальний код', max_length=50, unique=True)
    valid_from = models.DateTimeField('дійсне від')
    valid_to = models.DateTimeField('дійсне до')
    discount = models.IntegerField('Знижка', validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField('Дійсне')

    class Meta:
        verbose_name = 'Купон на знижку'
        verbose_name_plural = 'Купони на знижку'

    def __str__(self):
        return self.code

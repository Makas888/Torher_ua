from django.db import models


class ContactList(models.Model):
    """store contact information database model"""

    is_visible = models.BooleanField('активне', default=False)
    location_city = models.CharField('місто', max_length=50)
    location = models.CharField('адреса', max_length=250)
    post_index = models.CharField('поштовий індекс', max_length=15)
    open_days_start = models.CharField('перший робочий день', max_length=15)
    open_days_end = models.CharField('останній робочий день', max_length=15)
    open_hours_start = models.TimeField('початок робочого дня')
    open_hours_end = models.TimeField('кінець робочого дня')
    e_mail_1 = models.EmailField('перший E_mail')
    e_mail_2 = models.EmailField('другий E_mail', blank=True, default='')
    call_1 = models.CharField('номер телефона', max_length=15)
    call_2 = models.CharField('номер телефона', max_length=15, blank=True, null=True)
    link_map = models.TextField('посилання на мапу', max_length=500, blank=True, null=True)
    twitter = models.TextField(max_length=50, blank=True, null=True)
    facebook = models.TextField(max_length=50, blank=True, null=True)
    instagram = models.TextField(max_length=50, blank=True, null=True)
    telegram = models.TextField(max_length=50, blank=True, null=True)
    viber = models.TextField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'загальна інформація'
        verbose_name_plural = 'загальна інформація'

    def __str__(self):
        return f'Котакти магазину: варіант {self.pk}'


class UserMessage(models.Model):
    """a database model of messages from customers"""

    name = models.CharField("Ім'я", max_length=75)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=15)
    message = models.TextField('Повідомлення', max_length=500)

    archived = models.BooleanField('У архіві', default=False)
    date_in = models.DateTimeField('дата створення', auto_now_add=True)
    date_archiving = models.DateTimeField('остання дія', auto_now=True)

    class Meta:
        verbose_name = 'Повідомлення від клієнта'
        verbose_name_plural = 'Повідомлення від клієнта'
        ordering = ('archived', )

    def __str__(self):
        return f'{self.name} ({self.email}), {self.phone}: {self.message[:20]}'


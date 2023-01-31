from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from coupons.models import Coupon
from product.models import Product


class Order(models.Model):
    """
    database model for a specific order,
    the function of calculating the total cost of the order
    """

    first_name = models.CharField("Ім'я", max_length=50)
    last_name = models.CharField('Прізвище', max_length=50)
    email = models.EmailField()
    phone = models.CharField('Телефон', max_length=15)
    city = models.CharField('Місто', max_length=100)
    department_number = models.CharField('Номер відділення', max_length=20, blank=True, null=True)
    address = models.CharField('Адреса', max_length=250, blank=True, null=True)
    message = models.TextField('Повідомлення', blank=True, null=True)
    created = models.DateTimeField('дата створення', auto_now_add=True)
    updated = models.DateTimeField('змінено', auto_now=True)
    processed = models.BooleanField('Опрацьовано', default=False)
    coupon = models.ForeignKey(Coupon,
                               related_name='orders',
                               null=True,
                               blank=True,
                               on_delete=models.DO_NOTHING)
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f'Замовлення №{self.id} загальна сумма: {self.get_total_cost()}грн'

    def get_total_cost(self):
        total_coast = sum(item.get_cost() for item in self.items.all())
        total_coast_discount = total_coast - total_coast * (self.discount / Decimal('100'))
        return '{0:.2f}'.format(total_coast_discount)


class OrderItem(models.Model):
    """
    all products are tied to a specific user order,
    the function of calculating the total cost of the number of identical products
    """

    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity

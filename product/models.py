from django.db import models
import os
from uuid import uuid4
from django.urls import reverse


class SubCategory(models.Model):
    """product subcategory database model related to category many-to-many related to products one-to-many"""

    name = models.CharField('Назва категорії', max_length=256, unique=True)
    slug = models.SlugField(max_length=256, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Тип товару'
        verbose_name_plural = 'Тип товару'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product:product_list_by_category", args=[self.slug])


class Category(models.Model):
    """a product category database model associated with a many-to-many subcategory"""

    name = models.CharField('Назва категорії', max_length=256, unique=True)
    slug = models.SlugField(max_length=256, db_index=True, unique=True)
    parent = models.ManyToManyField(SubCategory, verbose_name='Тип товару')

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product:product_list_by_category", args=[self.slug])

    def quantity_product(self):
        """quantity of products in this category"""

        quantity = 0
        for item in self.parent.all():
            quantity += item.product_set.count()
        return quantity


class Brands(models.Model):
    """the product brand database model is related to product one-to-many"""

    name = models.CharField('Назва бренду', max_length=30, unique=True)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Список брендів'

    def __str__(self):
        return f'{self.name}'


class Discount(models.Model):
    """the product discount database model is related to product one-to-many"""

    percent = models.PositiveIntegerField('Знижка')

    class Meta:
        verbose_name_plural = 'Знижка товару'
        ordering = ('percent', )

    def __str__(self):
        return f'{self.percent}%'


class Product(models.Model):
    """product database model"""

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/product', f'{uuid4()}.{ext}')

    title = models.CharField('Назва товару', max_length=256, db_index=True)
    slug = models.SlugField(max_length=256, db_index=True, unique=True)
    desc = models.TextField('Опис товару', max_length=2000, blank=True)
    price = models.DecimalField('Вартість', max_digits=8, decimal_places=2)
    brand = models.ForeignKey(Brands, verbose_name='Торгова марка', on_delete=models.CASCADE)
    type_product = models.ForeignKey(SubCategory, verbose_name='Тип товару', on_delete=models.PROTECT)
    stock = models.PositiveIntegerField('Залишок на складі')
    size_length = models.PositiveSmallIntegerField('Длина')
    size_width = models.PositiveSmallIntegerField('Ширина')
    size_height = models.PositiveSmallIntegerField('Висота')
    color = models.CharField('Колір', max_length=50)
    material = models.CharField('Матеріал', max_length=25)
    discount = models.ForeignKey(Discount, verbose_name='Знижка "%"', on_delete=models.PROTECT)
    article = models.PositiveIntegerField('Артікул товару')
    image1 = models.ImageField('Зображення', upload_to=get_file_name, default='images/no_image.png')
    image2 = models.ImageField('Зображення', upload_to=get_file_name, default='images/no_image.png')
    image3 = models.ImageField('Зображення', upload_to=get_file_name, default='images/no_image.png')
    is_active = models.BooleanField('Наявність товару', default=True)

    price_with_discount = models.DecimalField('со скидкой', max_digits=8, decimal_places=2, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ('brand', 'is_active', 'price', 'stock', 'discount')
        index_together = (('id', 'slug'),)

    def save(self, *args, **kwargs):
        """calculates the discounted price"""

        self.price_with_discount = float(self.price * (100 - self.discount.percent) / 100)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product:product_detail", args=[self.id, self.slug])

    def __str__(self):
        return f'{self.title[:10]}: {self.brand}'

# Generated by Django 4.1.5 on 2023-01-25 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('brand', 'is_active', 'price', 'stock', 'discount'), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товари'},
        ),
    ]

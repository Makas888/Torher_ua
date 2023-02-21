# Generated by Django 4.1.6 on 2023-02-21 14:22

from django.db import migrations, models
import django.db.models.deletion
import home_page.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Заголовок')),
                ('desc', models.TextField(max_length=300, verbose_name='Опис')),
                ('photo', models.ImageField(upload_to=home_page.models.HeroSection.get_file_name, verbose_name='Фото')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Відображення')),
            ],
            options={
                'verbose_name': 'слайди у шапці',
                'verbose_name_plural': 'слайди у шапці',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=500, verbose_name='Опис новини')),
                ('image', models.ImageField(upload_to=home_page.models.News.get_file_name, verbose_name='Зображення')),
            ],
            options={
                'verbose_name': 'Новина',
                'verbose_name_plural': 'Новини',
            },
        ),
        migrations.CreateModel(
            name='NewsVisible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_visible', models.BooleanField(unique=True, verbose_name='Відобразити')),
                ('left_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='left_block', to='home_page.news', verbose_name='Лівий блок')),
                ('right_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='right_block', to='home_page.news', verbose_name='Правий блок')),
            ],
            options={
                'verbose_name': 'Відображення новин',
                'verbose_name_plural': 'Відображення новин',
                'ordering': ('-is_visible',),
            },
        ),
    ]

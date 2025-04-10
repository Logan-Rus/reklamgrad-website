# Generated by Django 5.1.7 on 2025-04-01 12:12

import django.utils.timezone
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата отправки')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_title', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', null=True, verbose_name='Название компании')),
                ('company_description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Описание компании')),
                ('contact_phone_title', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', null=True, verbose_name='Заголовок телефона')),
                ('contact_phone', models.CharField(default='', max_length=20, verbose_name='Телефон')),
                ('contact_email_title', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', null=True, verbose_name='Заголовок email')),
                ('contact_email', models.EmailField(default='', max_length=254, verbose_name='Email')),
                ('menu_nav_title', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', null=True, verbose_name='Заголовок меню навигации')),
                ('menu_services_title', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', null=True, verbose_name='Заголовок меню услуг')),
                ('menu_works_title', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', null=True, verbose_name='Заголовок меню работ')),
                ('social_vk_url', models.URLField(blank=True, default='', verbose_name='Ссылка VK')),
                ('copyright_text', django_ckeditor_5.fields.CKEditor5Field(default='', verbose_name='Текст копирайта')),
            ],
            options={
                'verbose_name': 'Футер',
                'verbose_name_plural': 'Футер',
            },
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Заголовок главной страницы')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', verbose_name='Описание главной страницы')),
                ('image', models.ImageField(upload_to='homepage/', verbose_name='Background-изображение главной страницы')),
                ('title_about', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Заголовок раздела О нас')),
                ('image_about', models.ImageField(upload_to='about/', verbose_name='Изображение')),
                ('description_about', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Описание раздела ')),
                ('advantage1_title', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Заголовок преимущества 1')),
                ('advantage1_description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Описание преимущества 1')),
                ('advantage2_title', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Заголовок преимущества 2')),
                ('advantage2_description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Описание преимущества 2')),
                ('advantage3_title', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Заголовок преимущества 3')),
                ('advantage3_description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Описание преимущества 3')),
                ('title_service', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Заголовок раздела Сервисы')),
                ('description_service', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Описание второго раздела')),
                ('title_work', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Заголовок раздела Работы')),
                ('description_work', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Описание третьего раздела')),
                ('contact_title', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Заголовок формы обратной связи')),
                ('contact_text', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Текст формы обратной связи')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главная страница',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('url', models.CharField(max_length=200, verbose_name='URL или якорь')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Пункт навигационного меню',
                'verbose_name_plural': 'Пункты навигационного меню',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', django_ckeditor_5.fields.CKEditor5Field(max_length=200, verbose_name='Название услуги')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', verbose_name='Описание')),
                ('image', models.ImageField(upload_to='services/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Данные об разделе Услуги',
                'verbose_name_plural': 'Данные об разделе Услуги',
            },
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('meta_title', models.CharField(blank=True, max_length=250, verbose_name='Мета-заголовок')),
                ('meta_description', models.TextField(blank=True, verbose_name='Мета-описание')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Статическая страница',
                'verbose_name_plural': 'Статические страницы',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', django_ckeditor_5.fields.CKEditor5Field(max_length=200, verbose_name='Название работы')),
                ('tip', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Тип работы')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', verbose_name='Описание')),
                ('image', models.ImageField(upload_to='works/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Данные об разделе Портфолио',
                'verbose_name_plural': 'Данные об разделе Портфолио',
            },
        ),
    ]

# Generated by Django 5.1.7 on 2025-04-01 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_staticpage_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainpage',
            name='contact_text',
        ),
    ]

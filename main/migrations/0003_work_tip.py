# Generated by Django 5.1.7 on 2025-03-14 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_collection_description_alter_work_description2'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='tip',
            field=models.TextField(blank=True, null=True, verbose_name=''),
        ),
    ]

# Generated by Django 3.2 on 2021-04-07 19:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время создания'),
            preserve_default=False,
        ),
    ]

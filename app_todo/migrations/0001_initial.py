# Generated by Django 3.2 on 2021-04-07 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='Название')),
                ('is_important', models.BooleanField(blank=True, default=False, verbose_name='Важная')),
                ('is_public', models.BooleanField(blank=True, default=False, verbose_name='Публичная')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Активно'), (1, 'Отложено'), (2, 'Выполнено')], default=0, verbose_name='Статус выполнения')),
                ('author', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, related_name='authors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

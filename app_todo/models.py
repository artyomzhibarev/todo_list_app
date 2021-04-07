from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    STATUS = (
        (0, 'Активно'),
        (1, 'Отложено'),
        (2, 'Выполнено'),
    )
    title = models.CharField(max_length=160, verbose_name='Название')
    is_important = models.BooleanField(default=False, blank=True, verbose_name='Важная')
    is_public = models.BooleanField(default=False, blank=True, verbose_name='Публичная')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    status = models.IntegerField(default=0, choices=STATUS, blank=True, verbose_name='Статус выполнения')
    author = models.ForeignKey(User, related_name='authors', on_delete=models.PROTECT, blank=True, default='')

from datetime import timedelta

import django
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


def _get_default_date():
    return timezone.now() + timedelta(days=1)


class Note(models.Model):
    class StatusType(models.TextChoices):
        ACTIVE = 'active', _('Активно')
        DRAFT = 'draft', _('Отложено')
        DONE = 'done', _('Выполнено')

    title = models.CharField(max_length=160, verbose_name='Название')
    important = models.BooleanField(default=False, verbose_name='Важная')
    public = models.BooleanField(default=False, blank=True, verbose_name='Публичная')
    create_at = models.DateTimeField('Дата', default=_get_default_date)
    status = models.CharField('Состояние', max_length=10, choices=StatusType.choices, default=StatusType.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    views = models.IntegerField('Количество просмотров', default=0)

    def __str__(self):
        return f'{self.title}'


# class Comment(models.Model):
#     NOTE_RATING = (
#         (0, 'Без оценки'),
#         (1, 'Ужасно'),
#         (2, 'Плохо'),
#         (3, 'Нормально'),
#         (4, 'Хорошо'),
#         (5, 'Отлично'),
#     )
#
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
#     note = models.ForeignKey(Note, on_delete=models.CASCADE, related_query_name='comments')
#     create_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
#     message = models.TextField(default='', blank=True, verbose_name='Комментарий')
#     rating = models.IntegerField(choices=NOTE_RATING, default=0, verbose_name='Оценка')
#
#     class Meta:
#         ordering = ('create_at',)


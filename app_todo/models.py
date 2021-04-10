from datetime import timedelta

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
    create_at = models.DateField('Дата', default=_get_default_date)
    status = models.CharField('Состояние', max_length=10, choices=StatusType.choices, default=StatusType.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    views = models.IntegerField('Количество просмотров', default=0)

    def __str__(self):
        return f'{self.title}'

    # class Meta:
    #     ordering = ('-create_at',)

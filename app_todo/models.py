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
    create_at = models.DateTimeField('Дата', default=_get_default_date)
    status = models.CharField('Состояние', max_length=10, choices=StatusType.choices, default=StatusType.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор',
                               related_name='my_notes')  # заметки конкретного автора
    views = models.IntegerField('Количество просмотров', default=0)
    readers = models.ManyToManyField(User, through='Comment', verbose_name='Читатели',
                                     related_name='notes')  # отмеченные заметки конкретным автором

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    NOTE_RATING = (
        (0, 'Без оценки'),
        (1, 'Ужасно'),
        (2, 'Плохо'),
        (3, 'Нормально'),
        (4, 'Хорошо'),
        (5, 'Отлично'),
    )

    commentator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Комментатор', default='')
    note = models.ForeignKey(Note, on_delete=models.CASCADE, verbose_name='Заметка')
    create_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    message = models.TextField(default='', blank=True, verbose_name='Комментарий')
    rating = models.PositiveIntegerField(choices=NOTE_RATING, default=0, verbose_name='Оценка', null=True)

    def __str__(self):
        return f'Commentator: {self.commentator}, note: {self.note}, rating: {self.rating}'

    class Meta:
        ordering = ('create_at',)

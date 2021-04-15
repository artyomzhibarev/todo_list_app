from django.contrib import admin

from django.contrib.admin import ModelAdmin

from .models import Note, Comment


@admin.register(Note)
class NoteAdmin(ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    pass

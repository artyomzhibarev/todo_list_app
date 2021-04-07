from .models import Note
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'is_important', 'create_at', 'is_public', 'status', 'author', )

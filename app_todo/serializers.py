from .models import Note
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    # author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    # author = serializers.PrimaryKeyRelatedField(read_only=True, default=AuthorSerializer())
    # author = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Note
        fields = ('id', 'title', 'important', 'public', 'create_at', 'status', 'author',)
        read_only_fields = ('author',)

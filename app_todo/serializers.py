from .models import Note, Comment
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comments = serializers.SlugRelatedField(slug_field='message', read_only=True)

    class Meta:
        model = Note
        fields = ('id', 'title', 'important', 'public', 'create_at', 'status', 'author', 'comments')
        # read_only_fields = ('author', 'create_at',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'note', 'message', 'rating')
        read_only_fields = ('commentator',)

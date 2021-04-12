from django.contrib.auth.models import User

from .models import Note
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.username')
    # comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Note
        fields = ('id', 'title', 'important', 'public', 'create_at', 'status',)

# class UserSerializer(serializers.ModelSerializer):
#     notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'notes', 'comments',)
#
#
# class CommentCreateSerializer(serializers.ModelSerializer):
#     author = serializers.ReadOnlyField(source='author.username')
#
#     class Meta:
#         model = Comment
#         fields = ('id', 'message', 'rating', 'author', 'note')

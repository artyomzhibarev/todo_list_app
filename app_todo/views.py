from django.shortcuts import render
from django.views import View
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from todo_list_app.settings_local import SERVER_VERSION
from .filters import NoteFilter, CommentFilter
from .models import Note, Comment
from .serializers import NoteSerializer, CommentCreateSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin


class NoteListModelViewSet(ReadOnlyModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    filterset_class = NoteFilter

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset if self.request.user.is_authenticated else queryset.filter(public=True)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if request.user.is_authenticated:
            notes = self.get_serializer(queryset, many=True)
        else:
            notes = self.get_serializer(queryset.filter(public=True), many=True)
        return Response(notes.data)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        if not request.user.is_authenticated:
            return Response(serializer.data, status=status.HTTP_403_FORBIDDEN)
        else:
            return super().retrieve(request, *args, **kwargs)


class NoteListCreateViewSet(RetrieveModelMixin,
                            CreateModelMixin,
                            UpdateModelMixin,
                            DestroyModelMixin,
                            GenericViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    permission_classes = (IsAuthenticated,)

    # def create(self, request, *args, **kwargs):
    #     serializer: NoteSerializer = self.get_serializer(data=request.data)
    #     if not serializer.is_valid():
    #         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     serializer.save(author=request.user)
    #     return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)


class CommentCreateViewSet(CreateModelMixin,
                           UpdateModelMixin,
                           DestroyModelMixin,
                           GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer: CommentCreateSerializer = self.get_serializer(data=request.data)
    #     if not serializer.is_valid():
    #         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     serializer.save(author=request.user)
    #     return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.validated_data['commentator'] = self.request.user
        serializer.save()


class CommentViewSet(ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_class = CommentFilter


class AboutView(View):
    def get(self, request):
        context = {
            'SERVER_VERSION': SERVER_VERSION,
            'current_user': request.user,
        }
        return render(request, template_name='about.html', context=context)

from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from .filters import NoteFilter
from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin


class NoteListModelViewSet(ReadOnlyModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    # filterset_class = NoteFilter

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset if self.request.user.is_authenticated else queryset.self.get_queryset().filter(public=True)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if request.user.is_authenticated:
            notes = self.get_serializer(queryset, many=True)
        else:
            notes = self.get_serializer(queryset.filter(public=True), many=True)
        return Response(notes.data)

    def retrieve(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return super().retrieve(request, *args, **kwargs)


class NoteListCreateViewSet(CreateModelMixin,
                            UpdateModelMixin,
                            DestroyModelMixin,
                            GenericViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer: NoteSerializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(author=request.user)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    # def destroy(self, request, *args, **kwargs):
    #     super().destroy(request, *args, **kwargs)
    #
    # def update(self, request, *args, **kwargs):
    #     super().update(request, *args, **kwargs)
    #
    # def partial_update(self, request, *args, **kwargs):
    #     super().partial_update(request, *args, **kwargs)

from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from .filters import NoteFilter
from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin


class NoteListModelViewSet(ReadOnlyModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (AllowAny,)

    filterset_class = NoteFilter

    # def get_object(self):
    #     obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
    #     self.check_object_permissions(self.request, obj)
    #     return obj

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

    def create(self, request, *args, **kwargs):
        serializer: NoteSerializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(author=request.user)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        note = self.get_object()
        if note.author == request.user:
            self.perform_destroy(note)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)


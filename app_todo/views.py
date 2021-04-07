from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = self.filter_queryset(Note.objects.filter(is_public=True))
        # filter_kwargs = {param: request.GET[param] for param in request.GET}
        # filter_queryset = queryset.filter(**filter_kwargs)
        # serializer = self.get_serializer(queryset, many=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

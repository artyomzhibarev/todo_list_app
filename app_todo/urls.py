from rest_framework import routers
from .views import NoteListModelViewSet, NoteListCreateViewSet

router = routers.SimpleRouter()
router.register(r'notes', NoteListModelViewSet, basename='notes')
router.register(r'note-create', NoteListCreateViewSet)

urlpatterns = router.urls

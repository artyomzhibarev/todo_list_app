from rest_framework import routers
from django.urls import path, include
from .views import NoteViewSet

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet, basename='notes')
urlpatterns = [
    path('', include(router.urls)),
]

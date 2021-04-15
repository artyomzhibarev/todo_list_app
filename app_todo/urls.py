from django.urls import path
from rest_framework import routers
from app_todo import views

router = routers.SimpleRouter()
router.register(r'notes', views.NoteListModelViewSet, basename='notes')
router.register(r'note-create', views.NoteListCreateViewSet, basename='create_note')
router.register(r'comment-create', views.CommentCreateViewSet, basename='create_message')
router.register(r'comments', views.CommentViewSet, basename='comments')
urlpatterns = router.urls

urlpatterns += [
    path('about/', views.AboutView.as_view(), name='about'),
                ]

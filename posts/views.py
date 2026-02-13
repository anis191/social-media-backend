from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from .permissions import *

class PostViewSet(ModelViewSet):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def get_queryset(self):
        return Post.objects.filter(
            author__profile__slug = self.kwargs.get('profile_slug')
        )

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class PostMediaViewSet(ModelViewSet):
    serializer_class = PostMediaSerializer
    permission_classes = [IsAuthenticated, IsPostOwnerForMediaCreate]

    def perform_create(self, serializer):
        serializer.save(post_id = self.kwargs.get("posts_pk"))

    def get_queryset(self):
        return PostMedia.objects.filter(
            post_id = self.kwargs.get("posts_pk")
        )

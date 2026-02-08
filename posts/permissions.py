from rest_framework import permissions
from .models import Post

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if obj.author == request.user:
            return True

class IsPostOwnerForMediaCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method not in permissions.SAFE_METHODS:
            post_id = view.kwargs.get("posts_pk")
            try:
                post = Post.objects.get(id = post_id)
            except Post.DoesNotExist:
                return False
            
            return post.author == request.user

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.post.author == request.user:
            return True

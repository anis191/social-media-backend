from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly

class UserProfileViewSet(ModelViewSet):
    http_method_names = ['get','put','patch']
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

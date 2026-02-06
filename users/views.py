from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# class UserViewSet(ModelViewSet):
    # queryset = User.objects.all()
    # serializer_class = UserSerializer

class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'slug'
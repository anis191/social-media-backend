from django.shortcuts import render
from .models import Reaction
from .serializers import *
from rest_framework.viewsets import ModelViewSet

class ReactionViewSet(ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer

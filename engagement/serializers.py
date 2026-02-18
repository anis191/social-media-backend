from rest_framework import serializers
from .models import Reaction

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['id','user','post','reaction','created_at']
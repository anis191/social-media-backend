from rest_framework import serializers
from .models import *

class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ['id','file','post','media_type','order','created_at']
        read_only_fields = ['post']

class PostSerializer(serializers.ModelSerializer):
    # media = PostMediaSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['id','author','content','visibility','is_edited','created_at','updated_at']
        read_only_fields = ['author']


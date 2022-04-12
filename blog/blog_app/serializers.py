from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', ]



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'content', 'image', 'created_at', 'updated_at', ]


    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['category'] = {
            'id': instance.category.id,
            'title': instance.category.title
        }

        return representation

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Category


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     content = serializers.CharField()
#     author = serializers.ReadOnlyField(source='author.username')
#
#     def create(self, validated_data):  # override method
#         return Post.objects.create(**validated_data)
#
#     def update(self, instance, validated_data): # override method
#         instance.id = validated_data.get("id", instance.id)
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         return instance
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author"]


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=40)
    metakeywords =  serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.metakeywords = validated_data.get("metakeywords", instance.metakeywords)
        instance.description = validated_data.get("description", instance.description)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        return instance


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')

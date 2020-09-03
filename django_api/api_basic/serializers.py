from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=20)
    kakao_id = serializers.CharField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.phone_number = validated_data.get('phone number', instance.phone_number)
        instance.kakao_id = validated_data.get('kakao id', instance.kakao-id)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
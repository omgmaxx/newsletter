from rest_framework import serializers

from app_news.models import *


class NewsletterSerializer(serializers.ModelSerializer):
    """Newsletter serializer for API"""
    filter_tag = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tag.objects.all())
    filter_code = serializers.SlugRelatedField(many=True, slug_field='name', queryset=PhoneCode.objects.all())

    class Meta:
        model = Newsletter
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    """Newsletter serializer for API"""
    tag = serializers.SlugRelatedField(slug_field='name', queryset=Tag.objects.all())
    code = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Client
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    """Phone code serializer for API"""
    client = serializers.SlugRelatedField(slug_field='phone_number', read_only=True)
    status = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Message
        fields = '__all__'


from rest_framework import serializers, fields

from app_news.models import *


class NewsletterSerializer(serializers.ModelSerializer):
    """Newsletter serializer for API"""
    filter_tag = serializers.StringRelatedField(many=True)
    filter_code = serializers.StringRelatedField(many=True)

    class Meta:
        model = Newsletter
        fields = ['id', 'created_at', 'text', 'filter_tag', 'filter_code', 'starts_at', 'ends_at']


class ClientSerializer(serializers.ModelSerializer):
    """Newsletter serializer for API"""

    class Meta:
        model = Client
        fields = ['id', 'phone_number', 'code', 'tag', 'GMT']
        read_only_fields = ('code',)


class TagSerializer(serializers.ModelSerializer):
    """Tag serializer for API"""

    class Meta:
        model = Tag
        fields = ['id', 'name']


class CodeSerializer(serializers.ModelSerializer):
    """Phone code serializer for API"""

    class Meta:
        model = PhoneCode
        fields = ['id', 'name']


class MessageSerializer(serializers.ModelSerializer):
    """Phone code serializer for API"""

    class Meta:
        model = Message
        fields = ['id', 'status', 'newsletter', 'client', 'sent']


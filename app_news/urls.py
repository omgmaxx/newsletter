from django.urls import path, include
from rest_framework import routers

from app_news.api import NewsletterViewSet, ClientViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'newsletters', NewsletterViewSet, basename='newsletters')
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = [
    path('', include(router.urls)),
]

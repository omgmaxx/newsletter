from django.urls import path, include
from rest_framework import routers

from app_news.api import NewsletterViewSet, ClientViewSet, MessageViewSet

router = routers.SimpleRouter()
router.register(r'newsletters', NewsletterViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

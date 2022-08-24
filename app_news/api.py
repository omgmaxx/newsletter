import logging

from rest_framework import viewsets

from app_news.models import *
from app_news.serializers import NewsletterSerializer, ClientSerializer, TagSerializer, \
    CodeSerializer, MessageSerializer

logger = logging.getLogger(__name__)


class NewsletterViewSet(viewsets.ModelViewSet):
    """Newsletters"""
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    # http_method_names = ('GET', 'POST', 'UPDATE', 'DELETE',)

    def get_name(self):
        return self.queryset.first().__class__.__name__

    def list(self, request, *args, **kwargs):
        """Getting list of newsletters"""
        logger.info(f'{self.get_name()} GET')
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Creating new newsletter"""
        logger.info(f'{self.name} POST')
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Deleting specific newsletter"""
        logger.warning(f'{self.name} DELETE')
        return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Getting info on specific newsletter"""
        logger.info(f'{self.name} GET')
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Updating specific newsletter"""
        logger.info(f'{self.name} PUT')
        return super().update(request, *args, **kwargs)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_name(self):
        return self.queryset.first().__class__.__name__

    def list(self, request, *args, **kwargs):
        """Getting list of client"""
        logger.info(f'{self.get_name()} GET')
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Creating new client"""
        logger.info(f'{self.name} POST')
        code = request.POST['phone_number'][:3]
        try:
            code = int(code)
        except ValueError:
            logger.error(f'{code} is not numeric')
        code_obj = PhoneCode.objects.get_or_create(name=code)[0]
        request.POST['code'] = code_obj.id
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Deleting specific client"""
        logger.warning(f'{self.name} DELETE')
        return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Getting info on specific client"""
        logger.info(f'{self.name} GET')
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Updating specific client"""
        logger.info(f'{self.name} PUT')
        return super().update(request, *args, **kwargs)


# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#
#     def get_name(self):
#         return self.queryset.first().__class__.__name__
#
#     def list(self, request, *args, **kwargs):
#         """Getting list of tag"""
#         logger.info(f'{self.get_name()} GET')
#         return super().list(request, *args, **kwargs)
#
#     def create(self, request, *args, **kwargs):
#         """Creating new tag"""
#         logger.info(f'{self.name} POST')
#         return super().create(request, *args, **kwargs)
#
#     def destroy(self, request, *args, **kwargs):
#         """Deleting specific tag"""
#         logger.warning(f'{self.name} DELETE')
#         return super().destroy(request, *args, **kwargs)
#
#     def retrieve(self, request, *args, **kwargs):
#         """Getting info on specific tag"""
#         logger.info(f'{self.name} GET')
#         return super().retrieve(request, *args, **kwargs)
#
#     def update(self, request, *args, **kwargs):
#         """Updating specific tag"""
#         logger.info(f'{self.name} PUT')
#         return super().update(request, *args, **kwargs)
#
#
# class CodeViewSet(viewsets.ModelViewSet):
#     queryset = PhoneCode.objects.all()
#     serializer_class = CodeSerializer
#
#     def get_name(self):
#         return self.queryset.first().__class__.__name__
#
#     def list(self, request, *args, **kwargs):
#         """Getting list of phone code"""
#         logger.info(f'{self.get_name()} GET')
#         return super().list(request, *args, **kwargs)
#
#     def create(self, request, *args, **kwargs):
#         """Creating new phone code"""
#         logger.info(f'{self.name} POST')
#         return super().create(request, *args, **kwargs)
#
#     def destroy(self, request, *args, **kwargs):
#         """Deleting specific phone code"""
#         logger.warning(f'{self.name} DELETE')
#         return super().destroy(request, *args, **kwargs)
#
#     def retrieve(self, request, *args, **kwargs):
#         """Getting info on specific phone code"""
#         logger.info(f'{self.name} GET')
#         return super().retrieve(request, *args, **kwargs)
#
#     def update(self, request, *args, **kwargs):
#         """Updating specific phone code"""
#         logger.info(f'{self.name} PUT')
#         return super().update(request, *args, **kwargs)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_name(self):
        return self.queryset.first().__class__.__name__

    def list(self, request, *args, **kwargs):
        """Getting list of message"""
        logger.info(f'{self.get_name()} GET')
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Creating new message"""
        logger.info(f'{self.name} POST')
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Deleting specific message"""
        logger.warning(f'{self.name} DELETE')
        return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Getting info on specific message"""
        logger.info(f'{self.name} GET')
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Updating specific message"""
        logger.info(f'{self.name} PUT')
        return super().update(request, *args, **kwargs)

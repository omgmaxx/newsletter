import logging

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

from app_news.models import *
from app_news.serializers import NewsletterSerializer, ClientSerializer, MessageSerializer
from app_news.services.client_viewset_create import ClientViewsetCreate

logger = logging.getLogger(__name__)


class NewsletterViewSet(viewsets.ModelViewSet):
    """
    Newsletter viewset

    Includes methods: GET, POST, PUT, DELETE
    """
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    http_method_names = ('get', 'post', 'put', 'delete')

    def get_name(self):
        return self.queryset.model.__name__

    @swagger_auto_schema(operation_summary="Getting list of newsletters", operation_description=' ')
    def list(self, request, *args, **kwargs):
        logger.info(f'[API] {self.get_name()} GET')
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Creating new newsletter", operation_description=' ')
    def create(self, request, *args, **kwargs):
        logger.info(f'[API] {self.get_name()} POST')
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Deleting specific newsletter", operation_description=' ')
    def destroy(self, request, *args, **kwargs):
        logger.warning(f'[API][Newsletter: {self.get_object().id}] DELETE')
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Getting info on specific newsletter", operation_description=' ')
    def retrieve(self, request, *args, **kwargs):
        logger.info(f'[API][Newsletter: {self.get_object().id}] GET')
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Updating specific newsletter", operation_description=' ')
    def update(self, request, *args, **kwargs):
        logger.info(f'[API][Newsletter: {self.get_object().id}] PUT {list(request.data)}')
        return super().update(request, *args, **kwargs)


class ClientViewSet(viewsets.ModelViewSet):
    """
    Clients viewset

    Includes methods: GET, POST, PUT, DELETE
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ('get', 'post', 'put', 'delete')

    def get_name(self):
        return self.queryset.model.__name__

    @swagger_auto_schema(operation_summary="Getting list of client", operation_description=' ')
    def list(self, request, *args, **kwargs):
        logger.info(f'[API] {self.get_name()} GET')
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Creating new client",
                         operation_description="Also generates object PhoneCode with "
                                               "first 3 characters of phone-number"
                                               "\n\n"
                                               "GMT range is -12 to +14")
    def create(self, request, *args, **kwargs):
        logger.info(f'[API] {self.get_name()} POST')
        code_obj = ClientViewsetCreate().execute(request.data['phone_number'])
        # super().create()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(code_id=code_obj.id)  # added code_id
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(operation_summary="Deleting specific client", operation_description=' ')
    def destroy(self, request, *args, **kwargs):
        logger.warning(f'[API][Client: {self.get_object().id}] DELETE')
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Getting info on specific client", operation_description=' ')
    def retrieve(self, request, *args, **kwargs):
        logger.info(f'[API][Client: {self.get_object().id}] GET')
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Updating specific client", operation_description=' ')
    def update(self, request, *args, **kwargs):
        logger.info(f'[API][Client: {self.get_object().id}] PUT {list(request.data)}')
        return super().update(request, *args, **kwargs)


class MessageViewSet(viewsets.ModelViewSet):
    """
    Message viewset

    Includes methods: GET
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ('get',)

    def get_name(self):
        return self.queryset.model.__name__

    @swagger_auto_schema(operation_summary="Getting list of message", operation_description=' ')
    def list(self, request, *args, **kwargs):
        logger.info(f'[API] {self.get_name()} GET')
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Getting info on specific message", operation_description=' ')
    def retrieve(self, request, *args, **kwargs):
        logger.info(f'[API][Message: {self.get_object().id}] GET')
        return super().retrieve(request, *args, **kwargs)

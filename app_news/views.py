from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin, \
    DestroyModelMixin

from app_news.models import Newsletter, Client
from app_news.serializers import NewsletterSerializer, ClientSerializer


# class NewsletterList(ListModelMixin, CreateModelMixin, GenericAPIView):
#     """List view of newsletters
#
#     Allows GET and POST"""
#     queryset = Newsletter.objects.all()
#     serializer_class = NewsletterSerializer
#
#     def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
#         """Getting list of newsletters"""
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
#         """Creating new newsletter"""
#         return self.create(request, *args, **kwargs)
#
#
# class NewsletterDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
#     """Detail view of newsletters
#
#     Allows GET, PUT and DELETE"""
#     queryset = Newsletter.objects.all()
#     serializer_class = NewsletterSerializer
#
#     def get(self, request, *args, **kwargs):
#         """Getting info on specific newsletter"""
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         """Updating specific newsletter"""
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         """Deleting specific newsletter"""
#         return self.destroy(request, *args, **kwargs)
#
#
# class ClientList(ListModelMixin, CreateModelMixin, GenericAPIView):
#     """List view of clients
#
#     Allows GET and POST"""
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#
#     def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
#         """Getting list of Clients"""
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
#         """Creating new client"""
#         print(request.POST['phone_number'])
#         return self.create(request, *args, **kwargs)
#
#
# class ClientDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
#     """Detail view of clients
#
#     Allows GET, PUT and DELETE"""
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#
#     def get(self, request, *args, **kwargs):
#         """Getting info on specific client"""
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         """Updating specific client"""
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         """Deleting specific client"""
#         return self.destroy(request, *args, **kwargs)
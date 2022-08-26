from django.contrib import admin

from app_news.models import *


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)


@admin.register(PhoneCode)
class PhoneCodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'tag', 'GMT', 'id',)
    list_filter = ('code', 'tag__name')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'starts_at', 'ends_at', 'get_tags', 'get_codes')
    list_filter = ('filter_tag', 'filter_code')

    def get_tags(self, obj):
        return [tag.name for tag in obj.filter_tag.all()]

    def get_codes(self, obj):
        return [tag.name for tag in obj.filter_code.all()]

    def get_text(self, obj):
        return obj.text[:100]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'client', 'sent', 'newsletter_id')
    list_filter = ('newsletter_id', 'status')
    search_fields = ('client__phone_number',)

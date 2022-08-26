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
    list_display = ('id', 'get_text', 'starts_at', 'ends_at', 'get_tags', 'get_codes', 'get_period')
    list_filter = ('filter_tag', 'filter_code')

    def get_tags(self, obj):
        return [tag.name for tag in obj.filter_tag.all()]

    get_tags.short_description = 'Tag'

    def get_codes(self, obj):
        return [tag.name for tag in obj.filter_code.all()]

    get_codes.short_description = 'Phone code'

    def get_text(self, obj):
        return obj.text[:50]

    get_text.short_description = 'Shortened text'

    def get_period(self, obj):
        if not obj.daily_start and not obj.daily_end:
            return 'Not set'
        return f'{obj.daily_start} -- {obj.daily_end}'

    get_text.short_description = 'Day period'


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'client', 'sent', 'newsletter_id')
    list_filter = ('newsletter_id', 'status')
    search_fields = ('client__phone_number',)
    actions = ['mark_as_in_process', 'mark_as_sent', 'mark_as_failed']

    def mark_as_in_process(self, request, queryset):
        queryset.update(status=1)

    def mark_as_sent(self, request, queryset):
        queryset.update(status=2)

    def mark_as_failed(self, request, queryset):
        queryset.update(status=3)

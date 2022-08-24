from django.contrib import admin

from app_news.models import *


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(PhoneCode)
class PhoneCodeAdmin(admin.ModelAdmin):
    pass

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    pass

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
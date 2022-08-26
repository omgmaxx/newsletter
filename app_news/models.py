from django.core.validators import MinLengthValidator
from django.db import models

from app_news.validators import validate_gmt, validate_phone_number


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')

    class Meta:
        db_table = 'Tag'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.name


class PhoneCode(models.Model):
    name = models.CharField(max_length=4, verbose_name='name')

    class Meta:
        db_table = 'Phone_code'
        verbose_name = 'phone_code'
        verbose_name_plural = 'phone_codes'

    def __str__(self):
        return self.name


class Client(models.Model):
    phone_number = models.CharField(max_length=10, verbose_name='phone number',
                                    validators=[validate_phone_number, MinLengthValidator(10)], unique=True)
    code = models.ForeignKey(PhoneCode, on_delete=models.CASCADE, verbose_name='country code', related_name='client')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='tag', related_name='client')
    GMT = models.IntegerField(verbose_name='GMT', validators=[validate_gmt])

    class Meta:
        db_table = 'Client'
        verbose_name = 'client'
        verbose_name_plural = 'clients'

    def __str__(self):
        return self.phone_number


class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    text = models.TextField(max_length=10000, verbose_name='text')
    filter_tag = models.ManyToManyField(Tag, related_name='newsletter', verbose_name='tag filter', blank=True)
    filter_code = models.ManyToManyField(PhoneCode, related_name='newsletter', verbose_name='code filter', blank=True)
    starts_at = models.DateTimeField(verbose_name='starts at')
    ends_at = models.DateTimeField(verbose_name='ends at', null=True, blank=True)
    daily_start = models.TimeField(verbose_name='daily start', null=True, blank=True)
    daily_end = models.TimeField(verbose_name='daily end', null=True, blank=True)

    class Meta:
        db_table = 'Newsletter'
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'

    def __str__(self):
        return f'№{self.id} newsletter'


class Status(models.Model):
    name = models.CharField(max_length=10, verbose_name='name')

    class Meta:
        db_table = 'Status'
        verbose_name = 'status'
        verbose_name_plural = 'statuses'

    def __str__(self):
        return self.name


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='name')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='status', related_name='message')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, verbose_name='newsletter',
                                   related_name='message')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='client', related_name='message')
    sent = models.DateTimeField(verbose_name='date of sending', null=True, blank=True)

    class Meta:
        db_table = 'Message'
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    def __str__(self):
        return f'Message for {self.client} of {self.newsletter.id} newsletter'

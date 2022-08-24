import logging
from datetime import datetime

import pytz
import requests
from django.db.transaction import atomic
from django.utils.timezone import now

from app_news.models import Newsletter, Message, Client, Status
from NewsLetterAPI.celery import app

logger = logging.getLogger(__name__)


@app.task(name='send_message')
def send_message(msg_id, phone, text):
    logger.info('Starting sending process')
    url = f'https://probe.fbrq.cloud/v1/send/{msg_id}'
    phone = ''.join(('+7', phone))
    data = {
        "id": msg_id,
        "phone": phone,
        "text": text,
    }
    # requests.post(data=data, url=url, headers=)
    logger.info(f'{data} is sent')

    message = Message.objects.get(id=msg_id)
    london_tz = pytz.timezone('Europe/London')
    cur_dt = london_tz.localize(datetime.now()).astimezone(pytz.UTC)
    message.status_id = 2
    message.sent = cur_dt
    message.save()


@app.task(name='send_message_starter', track_started=True)
def send_message_starter():
    logger.info('Started looking for active newsletters')

    london_tz = pytz.timezone('Europe/London')
    cur_dt = london_tz.localize(datetime.now()).astimezone(pytz.UTC)

    active_newsletters = Newsletter.objects.filter(starts_at__lte=cur_dt, ends_at__gte=cur_dt)
    logger.info(f'Active newsletters: {[str(ns) for ns in active_newsletters]}')

    for newsletter in active_newsletters:
        logger.info(f'Looking at newsletter: {newsletter}')
        client_list = Client.objects.filter(code__in=newsletter.filter_code.all(), tag__in=newsletter.filter_tag.all())
        logger.info(f'Active clients: {[client.phone_number for client in client_list]}')

        for client in client_list:
            message = Message.objects.get_or_create(client_id=client.id, newsletter_id=newsletter.id, defaults={'status_id': 1})[0]
            if message.status.id == 1:
                logger.info(f"{client}'s message is added to queue")
                send_message.apply_async(args=(message.id, client.phone_number, newsletter.text))

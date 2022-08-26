import json
from configparser import ConfigParser

import requests
from celery.utils.log import get_task_logger

from app_news.models import Message
from app_news.services.get_tz import GetTZ

logger = get_task_logger(__name__)
config = ConfigParser()
config.read('config.ini')


class SendMessageSrvc:
    """
    Sends message ('id', 'phone_number', 'text') to SMS sending API (probe.fbrq.cloud)

    """

    def _collect_args(self, msg_id: int, phone: str, text: str, references: str) -> tuple[str, dict[str], dict[str]]:
        """
        Collects arguments to send it to API

        :param msg_id: Message object id
        :param phone: Client's phone number
        :param text: Newsletter text
        :param references: Newsletter, message and client ID prepared for logging
        :return: url, data
        """
        logger.info(f'{references} Started collecting data')

        url = ''.join((config.get('sending_API', 'url'), str(msg_id)))
        phone = ''.join(('+7', str(phone)))
        data = {
            "id": msg_id,
            "phone": phone,
            "text": text,
        }
        token = config.get('sending_API', 'token')
        headers = {'Authorization': f'Bearer {token}'}
        return url, data, headers

    def _send_message(self, url: str, data: dict[str], msg_id: int, headers: dict[str], references: str) -> None:
        """
        Sends request to API

        :param url: URL address to API
        :param data: Collected data of message
        :param msg_id: Message object id
        :param references: Newsletter, message and client ID prepared for logging
        """
        logger.info(f'{references} Started preparing request for {url}')
        response = requests.post(data=json.dumps(data), url=url, headers=headers)
        if response.status_code == 200:
            logger.info(f'{references} {data} is sent (code: {response.status_code})')
            self._save_result(msg_id, references)
        else:
            logger.error(f'{references} {data} sending has failed (code: {response.status_code})')
            self._failed_result(msg_id, references)

    def _save_result(self, msg_id: int, references: str) -> None:
        """
        Changes message status to "sent" and saves current datetime

        :param msg_id: Message object id
        :param references: Newsletter, message and client ID prepared for logging
        """
        message = Message.objects.get(id=msg_id)
        cur_dt = GetTZ().execute()
        message.status_id = 2
        message.sent = cur_dt
        message.save(update_fields=["status", "sent"])
        logger.info(f'{references} (status: {message.status}) is saved successfully')

    def _failed_result(self, msg_id: int, references: str) -> None:
        """
        Changes message status to "failed" and saves current datetime

        :param msg_id: Message object id
        :param references: Newsletter, message and client ID prepared for logging
        """
        message = Message.objects.get(id=msg_id)
        message.status_id = 3
        message.save(update_fields=["status"])
        logger.info(f'{references} (status: {message.status}) is saved successfully')

    def execute(self, msg_id: int, ns_id: int, client_id: int, phone: str, text: str) -> None:
        """
        Executes sequence

        :param msg_id: Message object id
        :param ns_id: Newsletter's id
        :param client_id: Client's id
        :param phone: Client's phone number
        :param text: Newsletter text
        """
        references = f'[Newsletter: {ns_id}] [Message: {msg_id}] [Client: {client_id}]'
        logger.info(f'{references} Starting sending task')
        url, data, headers = self._collect_args(msg_id, phone, text, references)
        self._send_message(url, data, msg_id, headers, references)

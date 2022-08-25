import json
import logging

import requests

from app_news.models import Message
from app_news.services.get_tz import GetTZ

logger = logging.getLogger(__name__)


class SendMessageSrvc:
    """
    Sends message ('id', 'phone_number', 'text') to SMS sending API (probe.fbrq.cloud)

    """
    def _collect_args(self, msg_id: str, phone: str, text: str) -> tuple[str, dict[str], dict[str]]:
        """
        Collects arguments to send it to API

        :param msg_id: Message object id
        :param phone: Client's phone number
        :param text: Newsletter text
        :return: url, data
        """
        url = f'https://probe.fbrq.cloud/v1/send/{msg_id}'
        phone = ''.join(('+7', phone))
        data = {
            "id": msg_id,
            "phone": phone,
            "text": text,
        }
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9' \
                '.eyJleHAiOjE2OTI3OTEzMjQsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Ik9tZ2dtYXgifQ' \
                '.LsoaZfFj7UBLe4uRcHofB6mkqF50iW1D5d8aBsCt6VY '
        headers = {'Authorization': f'Bearer {token}'}
        return url, data, headers

    def _send_message(self, url: str, data: dict[str], msg_id: str, headers: dict[str]) -> None:
        """
        Sends request to API

        :param url: URL address to API
        :param data: Collected data of message
        :param msg_id: Message object id
        """
        response = requests.post(data=json.dumps(data), url=url, headers=headers)
        if response.status_code == 200:
            logger.info(f'{data} is sent (code: {response.status_code})')
            self._save_result(msg_id)
        else:
            logger.error(f'{data} sending has failed (code: {response.status_code})')
            self._failed_result(msg_id)

    def _save_result(self, msg_id: str) -> None:
        """
        Changes message status to "sent" and saves current datetime

        :param msg_id: Message object id
        """
        message = Message.objects.get(id=msg_id)
        cur_dt = GetTZ().execute()
        message.status_id = 2
        message.sent = cur_dt
        message.save(update_fields=["status", "sent"])
        logger.info(f'{message} (status: {message.status}) is saved successfully')

    def _failed_result(self, msg_id: str) -> None:
        """
        Changes message status to "failed" and saves current datetime

        :param msg_id: Message object id
        """
        message = Message.objects.get(id=msg_id)
        message.status_id = 3
        message.save(update_fields=["status"])
        logger.info(f'{message} (status: {message.status}) is saved successfully')

    def execute(self, msg_id: str, phone: str, text: str) -> None:
        """
        Executes sequence

        :param msg_id: Message object id
        :param phone: Client's phone number
        :param text: Newsletter text
        """
        logger.info('Starting sending process')
        url, data, headers = self._collect_args(msg_id, phone, text)
        self._send_message(url, data, msg_id, headers)

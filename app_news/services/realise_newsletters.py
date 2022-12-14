from configparser import ConfigParser

from celery.utils.log import get_task_logger

from app_news.models import Newsletter, Client, Message
from app_news.services.get_tz import GetTZ
from app_news.tasks.send_message import send_message

logger = get_task_logger(__name__)
config = ConfigParser()
config.read('config.ini')


class RealiseNewsletters:
    """
    Service that realises currently active newsletters

    """

    def _get_list_of_active_newsletters(self) -> None:
        """
        Gets currently active newsletters according to start_at and ends_at arguments

        """
        cur_dt = GetTZ().execute()
        logger.info('Started looking for active newsletters')
        active_newsletters = Newsletter.objects.filter(starts_at__lte=cur_dt, ends_at__gte=cur_dt)
        logger.info(f'Active newsletters: {[str(ns) for ns in active_newsletters]}')

        for newsletter in active_newsletters:
            self._get_list_of_related_clients(newsletter)

    def _get_list_of_related_clients(self, newsletter: Newsletter) -> None:
        """
        Gets clients that match tag and phonecode filters

        :param newsletter: Filtered Newsletter object
        """
        logger.info(f'Looking at newsletter: {newsletter}')
        client_list = Client.objects.filter(code__in=newsletter.filter_code.all(),
                                            tag__in=newsletter.filter_tag.all())
        logger.info(f'[Newsletter: {newsletter.id}] Active clients: {[client.phone_number for client in client_list]}')

        for client in client_list:
            self._send_message(client, newsletter)

    def _send_message(self, client: Client, newsletter: Newsletter) -> None:
        """
        Creates Message object and starts send_message async task

        :param client: Filtered Client object
        :param newsletter: Filtered Newsletter object
        """
        message = Message.objects.get_or_create(client_id=client.id, newsletter_id=newsletter.id,
                                                defaults={'status_id': 1})[0]

        cur_cl_time = GetTZ().execute(client.GMT).time()
        logger.info(f'[Client: {client.id}] Current time is {cur_cl_time}')

        # Returns if not time yet
        if newsletter.daily_start and newsletter.daily_end:
            if not newsletter.daily_start <= cur_cl_time <= newsletter.daily_end:
                logger.info(f"[Client: {client.id}] It's not time yet")
                return

        if message.status.id == 1:
            logger.info(f"[Newsletter: {newsletter.id}] [Message: {message.id}] [Client: {client.id}] {client}'s "
                        f"message is added to queue")
            send_message.apply_async(args=(message.id, newsletter.id, client.id, client.phone_number, newsletter.text))
        elif message.status.id == 3:
            if config.getboolean('backend', 'retrying_failed'):
                logger.info(f"[Newsletter: {newsletter.id}] [Message: {message.id}] [Client: {client.id}] {client}'s "
                            f"failed message is "
                            f"added to queue")
                send_message.apply_async(
                    args=(message.id, newsletter.id, client.id, client.phone_number, newsletter.text))

    def execute(self) -> None:
        """Executes sequence"""
        self._get_list_of_active_newsletters()

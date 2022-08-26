import logging

from app_news.models import PhoneCode

logger = logging.getLogger(__name__)


class ClientViewsetCreate:
    """
    Gets phone code from given phone number
    """

    def _generate_phone_code(self, phone_number: str) -> PhoneCode:
        """
        Gets phone code from given phone number

        :param phone_number: Client's phone number
        :return: PhoneCode object
        """
        code = phone_number[:3]
        try:
            code = int(code)
        except ValueError:
            logger.error(f'{code} is not numeric')
        return PhoneCode.objects.get_or_create(name=code)[0]

    def execute(self, phone_number: str) -> PhoneCode:
        """
        Executes sequence

        :param phone_number: Client's phone number
        :return: PhoneCode object
        """
        return self._generate_phone_code(phone_number)

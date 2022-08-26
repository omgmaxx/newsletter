from datetime import datetime, timedelta
from typing import Optional

from django.utils import timezone


class GetTZ:
    """
    Gets curent GMT time
    """

    def _get_tz(self, gmt_delta: int) -> datetime:
        """
        Gets curent GMT time

        :return: Datetime
        """
        utc = timezone.now()
        cur_dt = utc + timedelta(hours=gmt_delta)
        return cur_dt

    def execute(self, gmt_delta: Optional[int] = 3) -> datetime:
        """Executes sequence"""
        return self._get_tz(gmt_delta)

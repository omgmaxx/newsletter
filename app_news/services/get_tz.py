from datetime import datetime

import pytz


class GetTZ:
    """
    Gets curent GMT time
    """
    def _get_tz(self) -> datetime:
        """
        Gets curent GMT time

        :return: Datetime
        """
        local_tz = pytz.timezone('Europe/London')
        cur_dt = local_tz.localize(datetime.now()).astimezone(pytz.UTC)
        return cur_dt

    def execute(self) -> datetime:
        """Executes sequence"""
        return self._get_tz()

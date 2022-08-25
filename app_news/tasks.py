from NewsLetterAPI.celery import app
from app_news.services.realise_newsletters import RealiseNewsletters
from app_news.services.send_message_srvc import SendMessageSrvc


@app.task(name='send_message')
def send_message(msg_id: str, phone: str, text: str) -> None:
    """
    Task sending message to API

    :param msg_id: Message object id
    :param phone: Client's phone number
    :param text: Newsletter text
    """
    SendMessageSrvc().execute(msg_id, phone, text)


@app.task(name='send_message_starter', track_started=True)
def send_message_starter() -> None:
    """
    Task starting newsletter process
    """
    RealiseNewsletters().execute()

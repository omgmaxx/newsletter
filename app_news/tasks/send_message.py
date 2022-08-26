from NewsLetterAPI.celery import app
from app_news.services.send_message_srvc import SendMessageSrvc


@app.task(name='send_message')
def send_message(msg_id: int, ns_id: int, client_id: int, phone: str, text: str) -> None:
    """
    Task sending message to API

    :param msg_id: Message object id
    :param ns_id: Newsletter object id
    :param client_id: Client object id
    :param phone: Client's phone number
    :param text: Newsletter text
    """
    SendMessageSrvc().execute(msg_id, ns_id, client_id, phone, text)

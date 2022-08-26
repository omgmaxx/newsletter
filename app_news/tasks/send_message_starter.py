from NewsLetterAPI.celery import app
from app_news.services.realise_newsletters import RealiseNewsletters


@app.task(name='send_message_starter', track_started=True)
def send_message_starter() -> None:
    """
    Task starting newsletter process
    """
    RealiseNewsletters().execute()

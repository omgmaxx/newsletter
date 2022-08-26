# Nesletter API

## Structure

![db template image](docs/table.png)

## Commands

source venv/Scripts/activate

celery -A NewsLetterAPI beat -l info
celery -A NewsLetterAPI worker -l info -P gevent

celery -A NewsLetterAPI flower
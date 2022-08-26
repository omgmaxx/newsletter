# Newsletter API using django+celery


## Run

### Dependencies

- RabbitMQ (https://www.rabbitmq.com/download.html)
- Erlang (https://erlang.org/download/otp_versions_tree.html)
- Python > 3.10.4 (https://www.python.org/downloads/)
- Used windows10 + cygwin + bash

### Configurations

Are placed at /config.ini

- url
  - URL to message sender API
- token
  - Token to authenticate at sender API
- retrying_failed
  - True will try to send failed messages with every cycle
- period
  - Period between newsletter cycles in minutes

### Starting app

```sh
source venv/Scripts/activate

py manage.py migrate
py manage.py loaddata s_user.json
py manage.py loaddata statuses.json
py manage.py loaddata tags.json
py manage.py loaddata testing.json  # for testing purposes

py manage.py runserver  # for admin UI
```

### Launching newsletter

- Console №1
```sh
source venv/Scripts/activate

celery -A NewsLetterAPI beat -l info
```

- Console №2
```sh
source venv/Scripts/activate

celery -A NewsLetterAPI worker -l info -P gevent
```

## API

- Available methods are accessible at Swagger UI at /docs


## Links

- [address]/api  --  API
  - /api/newsletters/
  - /api/clients/
  - /api/messages/
- [address]/docs  --  swagger ui
- [address]/admin -- admin ui

## DB structure

![db template image](docs/table.png)

## Дополнительные задания

1) 
2) 
3) 
4) 
5) Swagger UI по ссылке /docs/
6) Admin UI по ссылке /admin/
7)  
8)  
9) При ошибке Message переводится в статус failed и повторяется при каждом цикле
10) 
11) Клиентам отправляется рассылка с учётом локального времени (основываясь на указанном GMT) в период, указанный в рассылке
12) Логирование API и бэкэнда рассылки (debug.log, error.log и консоль)
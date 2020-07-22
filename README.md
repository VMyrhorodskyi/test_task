## Run project

##### install requirements
[Python 3.7](https://www.python.org/downloads/), [Pipenv](https://pypi.org/project/pipenv/) and [Redis](https://redis.io/)

##### and follow the next steps
```bash
$ cd test_task/
$ pipenv install
$ pipenv shell
$ cd bitmex_gateway/
$ python manage.py runserver
``` 
##### then open `http://127.0.0.1:8000/` in your web browser in order to use Bitmex REST API gateway
##### or connect to `ws://localhost:8000/ws/` in order to use Bitmex Websocket API gateway and send
##### ```JSON: {"action": "subscribe", "account": <account_name>}``` to subscribe for Quotes updates or 
##### ```JSON: {"action": "unsubscribe", "account": <account_name>}``` to unsubscribe from Quotes updates
## Run project

##### install requirements
[Python 3.7](https://www.python.org/downloads/) and [Pipenv](https://pypi.org/project/pipenv/)

##### and follow the next steps
```bash
$ cd test_task/
$ pipenv install
$ pipenv shell
$ cd bitmex_gateway/
$ python manage.py runserver
``` 
##### then open `http://127.0.0.1:8000/` in your web browser in order to use Bitmex REST API gateway
##### or connect to `ws://localhost:8000/ws/quotes/` in order to use Bitmex Websocket API gateway and send
```{'action': 'subscribe', 'account': <account_name>}```
##### to subscribe for Quotes updates (for this purpose you can use some [websocket test client](https://chrome.google.com/webstore/detail/websocket-test-client/fgponpodhbmadfljofbimhhlengambbn?hl=en))
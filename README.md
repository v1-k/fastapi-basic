# FastAPI server

RESTful API based on FastAPI

- Authentication based on JWT
- Public/ Private API
- RabbitMQ w/ Celery Task scheduler
-

## Start RabbitMQ server

```
rabbitmq-server
```

## RabbitMQ server setup

```
    # add user 'test' and password 'test123'
    $ rabbitmqctl add_user test test123
    # add virtual host 'test_vhost'
    $ rabbitmqctl add_vhost test_vhost
    # add user tag 'test_tag' for user 'test'
    $ rabbitmqctl set_user_tags test test_tag
    # set permission for user 'test' on virtual host 'test_vhost'
    # three kinds of operations in RabbitMQ: configure, write and read
    $ rabbitmqctl set_permissions -p test_vhost test ".*" ".*" ".*"
```

## Start Celery worker

```
celery -A app.celeryTasks worker --loglevel=info
```

## Start FastAPI server

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn app.main:app
```

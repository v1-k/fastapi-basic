
from celery import Celery
from .. import config

USER = config.settings.rabbitmq_user
PASSWORD = config.settings.rabbitmq_password
LOCATION = config.settings.rabbitmq_location
VHOST = config.settings.rabbitmq_vhost

app = Celery('fast_api',
             broker='amqp://test:test123@localhost/test_vhost',
             backend='rpc://',
             include=['app.celeryTasks.tasks'])


from celery import Celery

app = Celery('fast_api',
             broker='amqp://test:test123@localhost/test_vhost',
             backend='rpc://',
             include=['app.celeryTasks.tasks'])

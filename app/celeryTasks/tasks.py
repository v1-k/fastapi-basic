from __future__ import absolute_import
from .celery import app
import time


@app.task
def background_task(x, y):

    return x + y

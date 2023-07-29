import os
from celery import Celery

CELERY_BROKER = os.environ.get('CELERY_BROKER', 'redis://redis:6379/0')
CELERY_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://redis:6379/1')

celery =  Celery('tasks', broker=CELERY_BROKER, backend=CELERY_BACKEND)

import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTING_MODULE','tgju.settings')
celery_app = Celery('tgju')
celery_app.config_from_object('django.conf:settings',namespace='CELERY')
celery_app.autodiscover_tasks()
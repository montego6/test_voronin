from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_voronin.settings')

app = Celery('test_voronin')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

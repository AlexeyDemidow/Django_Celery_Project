import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Celery_Project.settings')

app = Celery('Django_Celery_Project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-message-every-3-minutes': {
        'task': 'mailing.tasks.beat_mailing',
        'schedule': crontab(minute='*/3'),
    },
}
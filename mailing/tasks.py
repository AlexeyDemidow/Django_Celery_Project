from django.core.mail import send_mail
from Django_Celery_Project.celery import app
from .service import send_email
from .models import Recipient


@app.task
def send_mailing(user_email):
    send_email(user_email)


@app.task
def beat_mailing():
    for reciever in Recipient.objects.all():
        send_mail(
            'Тестовая рассылка',
            'Письмо приходит каждые 3 минуты',
            'django_fitapp@mail.ru',
            [reciever.email],
            fail_silently=False,
        )
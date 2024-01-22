from django.core.mail import send_mail


def send_email(user_email):
    send_mail(
        'Тестовая рассылка',
        'Вы успешно подписались на рассылку!',
        'django_fitapp@mail.ru',
        [user_email],
        fail_silently=False,
    )

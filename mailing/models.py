from django.db import models


class Recipient(models.Model):
    """Подписка на рассылку"""
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(max_length=99, verbose_name='Адрес электронной почты')

    def __str__(self):
        return self.name

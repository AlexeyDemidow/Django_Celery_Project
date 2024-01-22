from django.shortcuts import render
from django.views.generic import CreateView

from .models import Recipient
from .forms import RecipientForm
from .service import send_email
from .tasks import send_mailing


class RecipientView(CreateView):
    """Отображение формы подписки по email"""
    model = Recipient
    form_class = RecipientForm
    success_url = '/'
    template_name = 'recipient.html'

    def form_valid(self, form):
        form.save()
        # send_email(form.instance.email)
        send_mailing.delay(form.instance.email)  # нельзя импортировать объекты!!!
        return super().form_valid(form)

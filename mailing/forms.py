from django import forms
from .models import Recipient


class RecipientForm(forms.ModelForm):
    """Форма подписки по email"""
    class Meta:
        model = Recipient
        fields = '__all__'

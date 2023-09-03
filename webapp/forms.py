from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['owner', 'cvv', 'card_number', 'expiration_date_month', 'expiration_date_year']

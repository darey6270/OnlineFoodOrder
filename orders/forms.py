from django import forms
from .models import Order, PaymentModel


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'phone_no']

        #method for cleaning the data


class PaymentCreateForm(forms.ModelForm):
    class Meta:
        model = PaymentModel
        fields = ['email', 'card_number', 'card_date', 'card_name']

from django import forms

class CurrencyForm(forms.Form):
    amount = forms.DecimalField(label='Cantidad', max_digits=10, decimal_places=2)
    local_currency = forms.CharField(label='CLP', max_length=3)

from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type', 'description']
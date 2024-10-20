import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CurrencyForm
from .forms import TransactionForm
from .models import Transaction

def dashboard(request):
    ingresos = Transaction.objects.filter(user=request.user, transaction_type='Ingreso')
    egresos = Transaction.objects.filter(user=request.user, transaction_type='Egreso')

    total_ingresos = sum(trans.amount for trans in ingresos)
    total_egresos = sum(trans.amount for trans in egresos)

    context = {
        'total_ingresos': total_ingresos,
        'total_egresos': total_egresos,
        'ingresos_data': [trans.amount for trans in ingresos],
        'egresos_data': [trans.amount for trans in egresos]
    }
    return render(request, 'finanzas/dashboard.html', context)

import requests
from django.http import JsonResponse
from django.shortcuts import render
from .forms import CurrencyForm

def currency_conversion(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            local_currency = form.cleaned_data['local_currency'].upper()
            api_key = 'a97c09ef8be42bcbdc87dc16'  # Inserta tu clave de API
            url = f"https://api.exchangerate-api.com/v4/latest/{local_currency}"
            
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    rates = response.json().get('rates', {})
                    result = {
                        'USD': amount * rates.get('USD', 1),
                        'EUR': amount * rates.get('EUR', 1),
                        'GBP': amount * rates.get('GBP', 1),
                        'JPY': amount * rates.get('JPY', 1)
                    }
                    return JsonResponse({'success': True, 'result': result})
                else:
                    print(f"Error de la API, código de estado: {response.status_code}")
                    return JsonResponse({'success': False, 'error': 'Error al obtener datos de la API'})
            except Exception as e:
                print(f"Excepción al llamar a la API: {e}")
                return JsonResponse({'success': False, 'error': 'Error inesperado en la solicitud a la API'})
        else:
            print(f"Formulario inválido: {form.errors}")
            return JsonResponse({'success': False, 'error': 'Formulario no válido'})

    form = CurrencyForm()
    return render(request, 'finanzas/dashboard.html', {'form': form})

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user  # Asignar el usuario autenticado
            transaction.save()
            return redirect('dashboard')  # Redirige al dashboard tras guardar
    else:
        form = TransactionForm()
    
    transactions = Transaction.objects.filter(user=request.user)  # Obtén transacciones del usuario
    return render(request, 'finanzas/add_transaction.html', {'form': form, 'transactions': transactions})

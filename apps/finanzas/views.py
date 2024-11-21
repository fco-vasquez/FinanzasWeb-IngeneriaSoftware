import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CurrencyForm
from .forms import TransactionForm
from .models import Transaction

from django.shortcuts import render
import bcchapi
import pandas as pd
import numpy as np  # Asegúrate de tener numpy importado
from django.db import models


# Configurar la conexión a la API de BCCH
siete = bcchapi.Siete("nicolasveas68@gmail.com", "ISlu11fra#")

from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

"""
def dashboard2(request):
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
"""

import requests
from django.http import JsonResponse
from django.shortcuts import render
from .forms import CurrencyForm

import requests
from django.http import JsonResponse
from django.shortcuts import render
from .forms import CurrencyForm

def currency_conversion(request):
    # Usar 1 USD para la conversión
    amount = 1  # Comparar con 1 USD
    local_currency = 'USD'  # Establecemos la moneda base como el dólar
    api_key = 'a97c09ef8be42bcbdc87dc16'  # Inserta tu clave de API
    url = f"https://api.exchangerate-api.com/v4/latest/{local_currency}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            rates = response.json().get('rates', {})
            
            # Construir el resultado incluyendo más divisas
            result = {
                'USD': round(amount * rates.get('USD', 1), 2),
                'EUR': round(amount * rates.get('EUR', 1), 2),
                'GBP': round(amount * rates.get('GBP', 1), 2),
                'JPY': round(amount * rates.get('JPY', 1), 2),
                'AUD': round(amount * rates.get('AUD', 1), 2),  # Dólar australiano
                'CAD': round(amount * rates.get('CAD', 1), 2),  # Dólar canadiense
                'CNY': round(amount * rates.get('CNY', 1), 2),  # Yuan chino
                'BRL': round(amount * rates.get('BRL', 1), 2),  # Real brasileño
                'MXN': round(amount * rates.get('MXN', 1), 2),  # Peso mexicano
                'KRW': round(amount * rates.get('KRW', 1), 2),  # Won surcoreano
                'CLP': round(amount * rates.get('CLP', 1), 2)   # Peso chileno
            }

            return JsonResponse({'success': True, 'result': result})
        else:
            return JsonResponse({'success': False, 'error': 'Error al obtener datos de la API'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': 'Error inesperado en la solicitud a la API'})


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

#nuevo APIs bcchapi

def dashboard(request):
    # Datos de transacciones de ingresos y egresos
    ingresos = Transaction.objects.filter(user=request.user, transaction_type='Ingreso')
    egresos = Transaction.objects.filter(user=request.user, transaction_type='Egreso')

    total_ingresos = sum(trans.amount for trans in ingresos)
    total_egresos = sum(trans.amount for trans in egresos)

    ingresos_data = [trans.amount for trans in ingresos]
    egresos_data = [trans.amount for trans in egresos]

    # Consultar las series con el método cuadro de bcchapi
    cuadro = siete.cuadro(
        series=[
            "F021.M1.STO.N.CLP.0.M",  # M1
            "F021.FM2.STO.N.CLP.0.M",  # Fondos mutuos en M2
            "F033.FKF.PPB.Z.Z.2018.0.T",  # Formación bruta capital fijo real
            "F033.FBK.PPI.N.Z.2018.0.T",  # Formación bruta de capital trimestral
            "F033.FBK.PPI.N.Z.2018.0.A"   # Formación bruta de capital anual
        ],
        nombres=["m1", "fm2", "fbkf_real", "fbkf_trimestral", "fbkf_anual"],
        desde="2020-01-01",  # Últimos 4 años
        hasta="2023-12-31",
        frecuencia="M",
        observado={
            "m1": np.mean,  # Agregamos una función simple de promedio
            "fm2": np.mean,  # Lo mismo para FM2
            "fbkf_real": np.mean,  # Formación bruta capital fijo real
            "fbkf_trimestral": np.mean,  # Formación bruta de capital trimestral
            "fbkf_anual": np.mean  # Formación bruta de capital anual
        }
    )

    # Eliminar filas con valores NaN
    cuadro.dropna(inplace=True)

    # Formatear los valores para que solo muestren 2 decimales
    cuadro = cuadro.round(2)

    # Convertir índice (fechas) a una columna y formatear las fechas a mes y año
    cuadro.reset_index(inplace=True)
    cuadro['index'] = cuadro['index'].dt.strftime('%b %Y')  # Formato "Feb 2022", "Mar 2022", etc.

    # Convertir a diccionario para enviar a la plantilla
    datos_bcch = cuadro.to_dict(orient="records")

    # Unificar todo en el contexto
    context = {
        'total_ingresos': total_ingresos,
        'total_egresos': total_egresos,
        'ingresos_data': ingresos_data,
        'egresos_data': egresos_data,
        'datos_bcch': datos_bcch
    }

    return render(request, 'finanzas/dashboard.html', context)

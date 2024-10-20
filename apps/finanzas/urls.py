from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('actualizar/Finanzas', views.dashboard, name="dashboard"), # ejemplo xd
    #path('actualizar/Finanzas2', views.dashboard2, name="dashboard2"), # ejemplo xd
    path('actualizar/currency-conversion/', views.currency_conversion, name='currency_conversion'),
    path('actualizar/add/', views.add_transaction, name='add_transaction'),
]
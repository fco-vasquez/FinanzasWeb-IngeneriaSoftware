from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('Ingreso', 'Ingreso'),
        ('Egreso', 'Egreso')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPE)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"

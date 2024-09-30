from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create your models here.
#por medio del atributo user lo genero como forenkey vinculando perfil a usuario models.ForeignKey(User, on_delete=models.CASCADE)
#por otro lado asiendo una relacion de 1 a uno asociamos esto a borrar ambas tablas user = models.OneToOneField(User, on_delete=models.CASCADE)



#si se quiere agregar mas campos aqui es odne se realiza y en el html con los imput 
#ejemplo <input type="text" name="telefono" placeholder="Telefono" maxlength="9" pattern="[0-9]+" />


class Perfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario=models.CharField(max_length=45, null=True, blank=True,)
    direccion= models.CharField(max_length=45, null=True, blank=True)
    telefono = models.CharField(max_length=9, null=True, blank=True)
    edad = models.CharField(max_length=2, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    departamento = models.CharField(max_length=4, null=True, blank=True)
    GENERO = [
        ("H", "Hombre"),
        ("M", "Mujer"),
        ("O", "Otro"),
    ]
    genero = models.CharField(max_length=1, choices=GENERO)
    foto_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)  # Campo para la image

    def __str__(self):
        return f"{self.user.username}"
    
class Residente(models.Model):
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.perfil.user.username}'s Profile"

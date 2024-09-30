from django import forms
from apps.users.models import Perfil
from django import forms
from .models import Residente

class ActualizarPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['telefono', 'direccion', 'edad', 'fecha_nacimiento','departamento' , 'genero']

class ActualizarFotoForm(forms.ModelForm):
    class Meta:
        model = Residente
        fields = ['foto_perfil']
        widgets = {
            'foto_perfil': forms.FileInput(attrs={'accept': 'image/*'}),
        }


class PerfilForm(forms.ModelForm):
    class Meta:
        model= Perfil
        fields = '__all__'
    widgets = {
            'foto_perfil': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
        label='Contraseña'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña'}),
        label='Confirmar Contraseña'
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    #aqui se agregan para que salgan los nombres en los recuadros de los que estamos usando de los formularios defautl de django los que salen en el html como {{ form.username }}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Run','maxlength': '10'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Nombres'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Apellidos'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'type': 'email'})

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Run'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Run', 'maxlength': '10'})

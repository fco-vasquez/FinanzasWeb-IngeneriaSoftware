from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ActualizarPerfilForm, ActualizarFotoForm
from .models import Perfil
from .models import Residente
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
# Create your views here.


#importaciones de autenticanion , login, y cerrar sesion estos son de las librerias de django
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth import views as auth_views
#los decoradores nos sirven para pner permisos a ciertas funionalidades de la pagina como acceso al home entre otras se le pone @login_required antes de la funcion def
#from django.contrib.auth.decorators import login_required
#from django.shortcuts import render
#from models import Perfil aqui se mareo el django le tuve que poner la direccion exacta
#importamos la clase ususario de django
from django.contrib.auth.models import User

#acceso a paginas y resspuesta
from django.contrib.auth.decorators import login_required
from django.http import Http404

#enviar correos xd
from django.core.mail import send_mail

from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from .forms import RegistrationForm, LoginForm
from django.core.exceptions import ValidationError

login_required
def actualizar_perfil(request):
    try:
        perfil = get_object_or_404(Perfil, user=request.user)
        perfil_form = ActualizarPerfilForm(instance=perfil)
        foto_form = ActualizarFotoForm(instance=perfil)

        if request.method == 'POST':
            perfil_form = ActualizarPerfilForm(request.POST, instance=perfil)
            foto_form = ActualizarFotoForm(request.POST, request.FILES, instance=perfil)

            if perfil_form.is_valid() and foto_form.is_valid():
                perfil_form.save()
                foto_form.save()
                messages.success(request, "Perfil actualizado exitosamente.")
                return redirect('actualizar_perfil')  # Redirige a la página de actualización

        return render(request, 'users/actualizar_perfil.html', {
            'perfil': perfil,
            'perfil_form': perfil_form,
            'foto_form': foto_form
        })

    except Perfil.DoesNotExist:
        messages.info(request, "El usuario no tiene un perfil asociado.")
        return redirect('home')  # Redirige a la página principal o a donde prefieras
    except Exception as e:
        messages.error(request, f"Se produjo un error: {str(e)}")
        return redirect('home')  # Redirige a la página principal o a donde prefieras


# Create your views here.
def index(request):
    #es_podologo= request.user.groups.filter(name="podologo").exists()
    #es_secretaria= request.user.groups.filter(name="secretaria").exists() 
    #, {"es_podologo":es_podologo, "es_secretaria":es_secretaria}
    return render(request, "web/index.html")


def registro_login(request):
    form = RegistrationForm()
    login_form = LoginForm()
    msg = ""

    if request.method == 'POST':
        try:
            if 'register' in request.POST:
                form = RegistrationForm(request.POST, request.FILES)
                if form.is_valid():
                    user = form.save(commit=False)
                    user.set_password(form.cleaned_data['password1'])
                    user.save()

                    perfil = Perfil(
                        user=user,
                        usuario=user.username,
                        telefono=request.POST.get("telefono"),
                        direccion=request.POST.get("direccion"),
                        edad=request.POST.get("edad"),
                        fecha_nacimiento=request.POST.get("fecha_nacimiento") or None,
                        genero=request.POST.get("genero"),
                        foto_perfil=request.FILES.get("foto_perfil"),  # Guarda la imagen
                    )
                    perfil.save()

                    user = authenticate(username=user.username, password=form.cleaned_data['password1'])
                    if user is not None:
                        login(request, user)
                        return redirect("/")  # Redirige a la página principal o donde prefieras
                else:
                    msg = "Errores en el formulario de registro"
            
            elif 'login' in request.POST:
                login_form = LoginForm(request, data=request.POST)
                if login_form.is_valid():
                    user = login_form.get_user()
                    login(request, user)
                    return redirect("/")  # Redirige a la página principal o donde prefieras
                else:
                    msg = "Credenciales inválidas"
        
        except IntegrityError:
            msg = "Error de integridad en la base de datos. Por favor, intente de nuevo."
        except ValidationError as e:
            msg = f"Error de validación: {', '.join(e.messages)}"
        except Exception as e:
            msg = f"Se produjo un error inesperado: {str(e)}"

    return render(request, "users/registro.html", {
        "form": form,
        "login_form": login_form,
        "msg": msg,
        "lista_generos": Perfil.GENERO,
    })
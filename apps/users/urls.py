from django.urls import path

# login que django otoga a los usuario en el caso de no tener un proceso personalizado as view para cambairle el nombre  que no tenga conflictos con neustars vistas ya creadas
# path("login/", views.login_user, name="login"), vista cambiada

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('', views.index, name="home"),
    path('registro-login/', views.registro_login, name='registro_login'),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"),name="logout"),

    # URL para restablecer la contraseña
    path('resetear_password/', 
         auth_views.PasswordResetView.as_view(template_name="users/reset_password.html"), 
         name="resetear_password"),
    path('resetear_password_enviado/', 
         auth_views.PasswordResetDoneView.as_view(template_name="users/reset_password_sent.html"), 
         name="password_reset_done"),
    path('resetear/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="users/reset_password_confirm.html"), 
         name="password_reset_confirm"),
    path('resetear_password_completo/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="users/reset_password_complete.html"), 
         name="password_reset_complete"),
         
    path('actualizar/', views.actualizar_perfil, name='actualizar_perfil'),
]
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from apps.core import views as core_views
from apps.core.views import registrar, redirecionar_apos_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('disciplinas/', include('apps.disciplinas.urls')),
    path('atividades/', include('apps.atividades.urls')),
    path('professores/', include('apps.professores.urls')),
    path('progresso/', include('apps.progresso.urls')),
    path('comunidade/', include('apps.comunidade.urls')),
    path('registrar/', registrar, name='registrar'),
    
    # Rotas de Autenticação (Login/Logout)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('redirecionar/', core_views.redirecionar_apos_login, name='redirecionar_usuario'),
     # Recuperação de senha
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(
             template_name='registration/reset_password.html'
         ), name='reset_password'),

    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ), name='password_reset_confirm'),

    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ), name='password_reset_complete'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog_project import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Rota para o painel administrativo do Django
    path('admin/', admin.site.urls),

    # Rota para as URLs do aplicativo admin_app
    path('admin_app/', include('admin_app.urls')),

    # Página inicial do blog
    path('', views.home, name='home'),

    # Página de login do usuário
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Detalhes de uma notícia específica, identificada pelo ID
    path('noticia/<int:noticia_id>/', views.noticia_detalhe, name='noticia_detalhe'),

    # Rota para logout do usuário
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Página para adicionar uma nova notícia
    path('adicionar/', views.adicionar_noticia, name='adicionar_noticia'),

    # Página para criar uma nova conta de usuário
    path('create_account/', views.create_account, name='create_account'),

    # Página de perfil do usuário
    path('profile/', views.profile, name='profile'),

    # Página para editar uma notícia específica, identificada pelo ID
    path('noticia/<int:pk>/editar/', views.editar_noticia, name='editar_noticia'),

    # Página para apagar uma notícia específica, identificada pelo ID
    path('noticia/<int:pk>/apagar/', views.apagar_noticia, name='apagar_noticia'),

    # Rota para solicitar redefinição de senha
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="password_reset_form.html",email_template_name="password_reset_email.html",subject_template_name="password_reset_subject.txt"), name="password_reset"),

    # Página de confirmação de envio do email de redefinição de senha
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),

    # Página para redefinir a senha, acessada pelo link enviado no email
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),

    # Página de confirmação de redefinição de senha concluída
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
]

# Configuração para servir arquivos de mídia durante o desenvolvimento
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path,include
from . import views  # importa suas views locais
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # pelo menos uma rota
]

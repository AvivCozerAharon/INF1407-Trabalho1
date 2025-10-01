from django.urls import path
from . import views  # importa suas views locais

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # pelo menos uma rota
]

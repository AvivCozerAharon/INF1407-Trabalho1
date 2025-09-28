from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.adicionar_noticia, name='adicionar_noticia'),
]
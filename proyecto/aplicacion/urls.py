from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('iniciar/', views.iniciar, name='iniciar'),
    path('registrarse/', views.registrarse, name='registrarse'),
]
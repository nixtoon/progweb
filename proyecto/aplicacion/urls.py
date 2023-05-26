from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('iniciar/', views.iniciar, name='iniciar'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('checkout/', views.checkout, name='checkout'),
    path('pinturas/', views.pinturas, name='pinturas'),
]
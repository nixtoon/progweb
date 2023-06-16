from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('iniciar/', views.iniciar, name='iniciar'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('checkout/', views.checkout, name='checkout'),
    path('pinturas/', views.pinturas, name='pinturas'),
    path('escultura/', views.escultura, name='escultura'),
    path('orfebreria/', views.orfebreria, name='orfebreria'),
    path('tejidos/', views.tejidos, name='tejidos'),
    path('constanza/', views.constanza, name='constanza'),
    path('genesis/', views.genesis, name='genesis'),
    path('jose/', views.jose, name='jose'),
    path('mari/', views.mari, name='mari'),
    path('over_the_mind/', views.over_the_mind, name='over_the_mind'),
    path('san_helmut/', views.san_helmut, name='san_helmut'),
    path('otoño/', views.otoño, name='otoño'),
    path('manto/', views.manto, name='manto'),
    path('san_cisco/', views.san_cisco, name='san_cisco'),
    path('campana/', views.campana, name='campana'),
    path('album/', views.album, name='album'),
    path('nav/', views.nav, name='nav'),
    path('recuerdos_privados/', views.recuerdos_privados, name='recuerdos_privados'),
    path('obserbuho/', views.obserbuho, name='obserbuho'),
    path('pajaro/', views.pajaro, name='pajaro'),
    path('laguna_mental/', views.laguna_mental, name='laguna_mental'),
    path('dragon_fly/', views.dragon_fly, name='dragon_fly'),
    path('listar-obras/', views.listar_obras, name='listar_obras'),
    path('modificar-obras/<id>', views.modificar_obras, name='modificar_obras'),
    path('agregar-obras/', views.agregar_obras, name='agregar_obras'),
    path('eliminar_obras/<int:id>/', views.eliminar_obras, name='eliminar_obras'),
]
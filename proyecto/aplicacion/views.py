from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'app/index.html', context)

def contacto(request):
    context = {}
    return render(request, 'app/plantillas/contacto.html')

def iniciar(request):
    context = {}
    return render(request, 'app/plantillas/iniciar.html')

def registrarse(request):
    context = {}
    return render(request, 'app/plantillas/registrarse.html')

def checkout(request):
    context = {}
    return render(request, 'app/plantillas/checkout.html')

# views de las categorias

def  pinturas(request):
    context = {}
    return render(request, 'app/plantillas/categorias/pinturas.html')

def escultura(request):
    context = {}
    return render(request, 'app/plantillas/categorias/escultura.html')

def orfebreria(request):
    context = {}
    return render(request, 'app/plantillas/categorias/orfebreria.html')

def tejidos(request):
    return render(request, 'app/plantillas/categorias/tejidos.html')


# views de los artistas

def constanza(request):
    return render(request, 'app/plantillas/artistas/constanza.html')

def genesis(request):
    return render(request, 'app/plantillas/artistas/genesis.html')

def jose(request):
    return render(request, 'app/plantillas/artistas/jose.html')

def mari(request):
    return render(request, 'app/plantillas/artistas/mari.html')


# views de las obras

def over_the_mind(request):
    return render(request, 'app/plantillas/obras/pinturas/over_the_mind.html')

def san_helmut(request):
    return render(request, 'app/plantillas/obras/esculturas/san_helmut.html')

def otoño(request):
    return render(request, 'app/plantillas/obras/orfebreria/otoño.html')

def manto(request):
    return render(request, 'app/plantillas/obras/tejidos/manto.html')

def san_cisco(request):
    return render(request, 'app/plantillas/obras/pinturas/san_cisco.html')

def campana(request):
    return render(request, 'app/plantillas/obras/orfebreria/campana.html')

def album(request):
    return render(request, 'app/plantillas/obras/pinturas/album.html')

def nav(request):
    return render(request, 'app/plantillas/obras/esculturas/nav.html')

def recuerdos_privados(request):
    return render(request, 'app/plantillas/obras/pinturas/recuerdos_privados.html')

def obserbuho(request):
    return render(request, 'app/plantillas/obras/esculturas/obserbuho.html')

def pajaro(request):
    return render(request, 'app/plantillas/obras/orfebreria/pajaro.html')

def laguna_mental(request):
    return render(request, 'app/plantillas/obras/esculturas/laguna_mental.html')

def dragon_fly(request):
    return render(request, 'app/plantillas/obras/orfebreria/dragon_fly.html')
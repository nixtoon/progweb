from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

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

def iniciar_artista(request):
    context = {}
    return render(request, 'app/plantillas/iniciar_artista.html')

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

#crud obras

def agregar_obras(request):
    categorias = Categoria.objects.all()
    artistas   = Artista.objects.all()

    data = {
        'categorias': categorias,
        'artistas'  : artistas
    }

    if request.method == 'POST':

        titulo           = request.POST["titulo"]
        categoria        = request.POST["categoria"]
        artista          = request.POST["artista"]
        precio           = request.POST["precio"]
        fechaPublicacion = request.POST["fecha"]
        descripcion      = request.POST["descripcion"]

        objCategoria = Categoria.objects.get(id = categoria)
        objArtista   = Artista.objects.get(rut = artista)

        obra = Obra.objects.create(
            titulo            = titulo,
            precio            = precio,
            descripcion       = descripcion,
            fecha_publicacion = fechaPublicacion,
            categoria         = objCategoria,
            artista           = objArtista,
        )
  
        if 'imagen' in request.FILES:
            imagen      = request.FILES['imagen']
            obra.imagen = imagen
            obra.save()
            messages.success(request, 'Obra registrada correctamente')
        else:
            messages.warning(request, 'No se ha seleccionado ninguna imagen')

        return redirect(to='listar_obras')

    return render(request, 'app/plantillas/crud_obras/agregar.html', data)

def listar_obras(request):
    obras = Obra.objects.all()

    data = {
        'obras': obras
    }

    return render(request, 'app/plantillas/crud_obras/listar.html', data)


def modificar_obras(request, id):
    obra       = get_object_or_404(Obra, id= id)
    categorias = Categoria.objects.all()
    artistas   = Artista.objects.all()

    if request.method == 'POST':
        titulo            = request.POST['titulo']
        categoria         = request.POST['categoria']
        artista           = request.POST['artista']
        precio            = request.POST['precio']
        fecha_publicacion = request.POST['fecha']
        descripcion       = request.POST['descripcion']
        
        objCategoria = Categoria.objects.get(id = categoria)
        objArtista   = Artista.objects.get(rut = artista)

        obra.titulo            = titulo
        obra.categoria         = objCategoria
        obra.artista           = objArtista
        obra.precio            = precio
        obra.fecha_publicacion = fecha_publicacion
        obra.descripcion       = descripcion
        
        if 'imagen' in request.FILES:
            imagen      = request.FILES['imagen']
            obra.imagen = imagen
        
        obra.save()
        messages.success(request, 'Obra modificada correctamente')
        return redirect('listar_obras')
    
    data = {
        'obra'      : obra,
        'categorias': categorias,
        'artistas'  : artistas,
    }
    return render(request, 'app/plantillas/crud_obras/modificar.html', data)

def eliminar_obras(request, id):

    try:
        obra = get_object_or_404(Obra, id= id)
        obra.delete()
        messages.success(request, "Eliminado Correctamente")
        obras = Obra.objects.all()

        data = {
            'obras': obras,
        }

        return render(request, 'app/plantillas/crud_obras/listar.html', data)
    
    except:
        messages.warning(request, "Error al eliminar")

        obras = Obra.objects.all()

        data = {
            'obras': obras,
        }

        return render(request, 'app/plantillas/crud_obras/listar.html', data)
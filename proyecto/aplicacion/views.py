from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'app/index.html', context)

def contacto(request):
    return render(request, 'app/plantillas/contacto.html')

def iniciar(request):
    return render(request, 'app/plantillas/iniciar.html')

def registrarse(request):
    return render(request, 'app/plantillas/registrarse.html')
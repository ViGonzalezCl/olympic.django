from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto, Categoria

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')
#def catalogofutbol(request):
    #return render(request, 'myapp/catalogofutbol.html')
#def catalogogym(request):
    #return render(request, 'myapp/catalogogym.html')
#def catalogotennis(request):
    #return render(request, 'myapp/catalogotennis.html')
def contacto(request):
    return render(request, 'myapp/contacto.html')
def crearCuenta(request):
    return render(request, 'myapp/crearCuenta.html')
def futbol(request):
    return render(request, 'myapp/futbol.html')
def gym(request):
    return render(request, 'myapp/gym.html')
def nosotros(request):
    return render(request, 'myapp/nosotros.html')
def sucursales(request):
    return render(request, 'myapp/sucursales.html')
def carro(request):
    return render(request, 'myapp/carro.html')


#######LISTAR CATALOGOS

def catalogotennis(request):
    productos= Producto.objects.raw("select * from myapp_producto where idCategoria = 4")
    context={"productos":productos}

    return render(request, 'myapp/catalogotennis.html', context)

def catalogogym(request):
    productos= Producto.objects.raw("select * from myapp_producto where idCategoria = 5")
    context={"productos":productos}

    return render(request, 'myapp/catalogogym.html', context)

def catalogofutbol(request):
    productos= Producto.objects.raw("select * from myapp_producto where idCategoria = 1")
    context={"productos":productos}

    return render(request, 'myapp/catalogofutbol.html', context)
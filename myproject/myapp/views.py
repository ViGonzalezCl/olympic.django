from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto, Categoria
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')
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


"""
###INDEX 
@login_required
def index(request):

    request.session["usuario"]="usuario1"
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'myapp/index.html', context)"""


#######LISTAR CATALOGOS

def catalogotennis(request):
    productos= Producto.objects.raw("select * from myapp_producto where id_categoria = 4")
    context={"productos":productos}

    return render(request, 'myapp/catalogotennis.html', context)

def catalogogym(request):
    productos= Producto.objects.raw("select * from myapp_producto where id_categoria = 5")
    context={"productos":productos}

    return render(request, 'myapp/catalogogym.html', context)

def catalogofutbol(request):
    productos= Producto.objects.raw("select * from myapp_producto where id_categoria = 1")
    context={"productos":productos}

    return render(request, 'myapp/catalogofutbol.html', context)

######CRUD

def crud(request): 
    productos= Producto.objects.all()
    context= {'productos':productos}
    
    return render(request, 'myapp/productos_list.html', context)

def productosAdd(request):

    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = ProductoForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
        form.save()

        #limpiar form
        form=ProductoForm()

        context={'mensaje': "OK, datos grabados...","form":form}
        return render(request, 'myapp/productos_add.html', context)
    else:
        form = ProductoForm()
        context={'form':form}
        return render(request, 'myapp/productos_add.html', context)

def productos_del(request,pk):
    context={}
    try:
        producto=Producto.objects.get(id=pk)
        producto.delete()
        mensaje="Producto Eliminado Correctamente"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
        return render(request, 'myapp/productos_list.html', context)
    except:
        mensaje="Error, producto no existe..."
        productos = Producto.objects.all()
        context = {'productos': producto, 'mensaje': mensaje}
        return render(request, 'myapp/productos_list', context)
    
def productos_findEdit(request,pk):
    if pk != "":
        producto= Producto.objects.get(id=pk)
        categorias= Categoria.objects.all()

        print(type(producto.id_categoria.categoria))

        context={'producto':producto, 'categorias':categorias}
        if producto:
            return render(request, 'myapp/productos_edit.html', context)
        else:
            context={'mensaje':"Error, producto no existe"}
            return render(request, 'myapp/productos_list.html', context)
        
        
def productosUpdate(request):
    if request.method == "POST":
        nombre_producto=request.POST['nombre']
        precio=request.POST['precio']
        descripcion=request.POST['descripcion']
        url_imagen=request.POST['imagen']
        categoria=request.POST['categoria']
        activo="1"

        objCategoria=Categoria.objects.get(id_categoria = categoria)

        producto = Producto()
        producto.nombre_producto=nombre_producto
        producto.precio=precio
        producto.descripcion=descripcion
        producto.url_imagen=url_imagen
        producto.id_categoria=objCategoria
        producto.activo=1
        producto.save()

        categorias=Categoria.objects.all()
        context={'mensaje': "ok, datos actualizados", 'categorias':categorias, 'producto':producto}
        return render(request, 'myapp/productos_edit.html', context)
    else:
        productos= Producto.objects.all()
        context={'productos':productos}
        return render(request, 'myapp/productos_list.html', context)
    

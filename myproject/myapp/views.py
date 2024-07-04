from django.shortcuts import render, redirect
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
    if request.method != "POST":
        categorias = Categoria.objects.all()
        context ={'categorias':categorias}
        return render(request, 'myapp/productos_add.html', context)
    
    else:
        nombre_producto=request.POST["nombre_producto"]
        precio=request.POST["precio"]
        descripcion=request.POST["descripcion"]
        imagen=request.POST["imagen"]
        categoria=request.POST["categoria"]

        objCategoria=Categoria.objects.get(id_categoria = categoria)
        obj=Producto.objects.create(    nombre_producto=nombre_producto,
                                        precio=precio,
                                        descripcion=descripcion,
                                        url_imagen=imagen,
                                        id_categoria=objCategoria
                                    )
        obj.save()
        categorias = Categoria.objects.all()
        context={'mensaje': "Datos agregados exitosamente",'categorias':categorias}
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
        nombre_producto=request.POST["nombre"]
        precio=request.POST["precio"]
        descripcion=request.POST["descripcion"]
        url_imagen=request.POST["imagen"]
        categoria=request.POST["categoria"]
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
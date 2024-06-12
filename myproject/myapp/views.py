from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def catalogofutbolbalones(request):
    return render(request, 'myapp/catalogofutbolbalones.html')

def catalogofutbolimplementos(request):
    return render(request, 'myapp/catalogofutbolimplementos.html')

def catalogofutbolropa(request):
    return render(request, 'myapp/catalogofutbolropa.html')

def catalogogymaccesorios(request):
    return render(request, 'myapp/catalogogymaccesorios.html')

def catalagogymhombre(request):
    return render(request, 'myapp/catalagogymhombre.html')

def catalogogymmujer(request):
    return render(request, 'myapp/catalogogymmujer.html')

def catalogotennishombre(request):
    return render(request, 'myapp/catalogotennishombre.html')

def catalogotennismujer(request):
    return render(request, 'myapp/catalogotennismujer.html')

def catalogotennisraqueta(request):
    return render(request, 'myapp/catalogotennisraqueta.html')

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

def tennis(request):
    return render(request, 'myapp/tennis.html')

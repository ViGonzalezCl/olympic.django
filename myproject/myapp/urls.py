from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Maneja la URL vacía y asigna la vista 'index' a esa URL
    path('catalogofutbol/', views.catalogofutbol, name='catalogofutbol'),
    path('catalogogym/', views.catalogogym, name='catalogogym'),
    path('catalogotennis/', views.catalogotennis, name='catalogotennis'),
    path('contacto/', views.contacto, name='contacto'),
    path('crearCuenta/', views.crearCuenta, name='crearCuenta'),
    path('futbol/', views.futbol, name='futbol'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('sucursales/', views.sucursales, name='sucursales'),
    #path('carro', views.carro, name="carro"),
 
    ##CRUD

    path('crud', views.crud, name='crud'),
    path('productosAdd', views.productosAdd, name='productosAdd'),
    path('productos_del/<int:pk>', views.productos_del, name='productos_del'),   
    path('productos_findEdit/<int:pk>', views.productos_findEdit, name='productos_findEdit'),
    path('productosUpdate', views.productosUpdate, name='productosUpdate'),

    ]

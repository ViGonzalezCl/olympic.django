from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Maneja la URL vacía y asigna la vista 'index' a esa URL
    path('catalogofutbolbalones/', views.catalogofutbolbalones, name='catalogofutbolbalones'),
    path('catalogofutbolimplementos/', views.catalogofutbolimplementos, name='catalogofutbolimplementos'),
    path('catalogofutbolropa/', views.catalogofutbolropa, name='catalogofutbolropa'),
    path('catalogogymaccesorios/', views.catalogogymaccesorios, name='catalogogymaccesorios'),
    path('catalagogymhombre/', views.catalagogymhombre, name='catalogogymhombre'),
    path('catalogogymmujer/', views.catalogogymmujer, name='catalogogymmujer'),
    path('catalogotennishombre/', views.catalogotennishombre, name='catalogotennishombre'),
    path('catalogotennismujer/', views.catalogotennismujer, name='catalogotennismujer'),
    path('catalogotennisraqueta/', views.catalogotennisraqueta, name='catalogotennisraqueta'),
    path('contacto/', views.contacto, name='contacto'),
    path('crearCuenta/', views.crearCuenta, name='crearCuenta'),
    path('futbol/', views.futbol, name='futbol'),
    path('gym/', views.gym, name='gym'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('tennis/', views.tennis, name='tennis'),
]


from django.contrib import admin
from django.urls import path
from gestionPedidos import views

urlpatterns=[
	path('admin/',admin.site.urls),
	path('busqueda_productos/',views.busqueda_productos),
	path('buscar/',views.buscar),
	path('contacto/',views.contacto),
]

from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos


class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono",)
    search_fields = ("nombre", "telefono",)  # Buscar por nombre y telefono


class ArticulosAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    list_filter = ("seccion",)


class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha",)
    list_filter = ("fecha",)
    date_hierarchy = "fecha"


admin.site.register(Pedidos, PedidosAdmin)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)

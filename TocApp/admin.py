from django.contrib import admin
from .models import *

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreCompleto', 'run', 'Cargo', 'Contrato', )
    ordering = ('nombreCompleto', )
    search_fields = ('nombreCompleto', )
    list_editable = ('Cargo', 'Contrato', )
    list_display_links = ('nombreCompleto', )
    list_filter = ('Cargo', )
    list_per_page = (8)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreProd', 'nombreTipo', 'precio', )
    ordering = ('nombreProd', )
    search_fields = ('nombreProd', 'nombreTipo' )
    list_editable = ('precio', )
    list_display_links = ('nombreProd', )
    list_filter = ('nombreTipo', )
    list_per_page = (8)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_cliente', 'modo_entrega', 'estado', 'total' )
    ordering = ('nombre_cliente', )
    search_fields = ('nombre_cliente', )
    list_editable = ('modo_entrega', 'estado', )
    list_display_links = ('nombre_cliente', )
    list_filter = ('estado', )
    list_per_page = (8)

@admin.register(Combo)
class ComboAdmin(admin.ModelAdmin):
    list_display = ('id','producto1','producto2','producto3','nombreCombo', 'precioCombo')
    ordering = ('nombreCombo', )
    search_fields = ('nombreCombo', )
    list_editable = ('precioCombo', )
    list_display_links = ('nombreCombo', )
    list_filter = ('nombreCombo', 'precioCombo', )
    list_per_page = (8)


#admin.site.register(Combo)
#admin.site.register(Pedido)

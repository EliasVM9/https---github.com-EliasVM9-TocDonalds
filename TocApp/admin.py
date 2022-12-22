from django.contrib import admin
from .models import *
class ComboProductoInline(admin.TabularInline):
    model = ComboProducto
    extra = 0
class ComboAdmin(admin.ModelAdmin):
    inlines = (ComboProductoInline,)
class ProductoAdmin(admin.ModelAdmin):
    inlines = (ComboProductoInline,)

class VentaComboInline(admin.TabularInline):
    model = VentaCombo
    extra = 0

class VentaProductoInline(admin.TabularInline):
    model = VentaProducto
    extra = 0
class VentaAdmin(admin.ModelAdmin):
    inlines = (VentaComboInline, VentaProductoInline,)



admin.site.register(Producto)
admin.site.register(Combo, ComboAdmin)
admin.site.register(Venta, VentaAdmin)
#admin.site.register(ComboProducto)
admin.site.register(Trabajador)
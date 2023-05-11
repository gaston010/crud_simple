from django.contrib import admin
from .models import Proveedor, Producto
# Register your models here.


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni')
    search_fields = ('nombre', 'apellido', 'dni')
    list_filter = ('nombre','dni')

admin.site.register(Proveedor, ProveedorAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock_actual', 'proveedor')
    search_fields = ('nombre', 'precio', 'stock_actual', 'proveedor')
    list_filter = ('nombre','proveedor')


admin.site.register(Producto, ProductoAdmin)

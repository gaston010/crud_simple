from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .models import Producto, Proveedor

# Create your views here.

#create the main page view
def index(request):
    return render(request, 'index.html')



def product_list(request):
    data = []
    products = Producto.objects.all()
    for items in products:
        content  ={
            'nombre': items.nombre,
            'precio': items.precio,
            'stock_actual': items.stock_actual,
            'proveedor': items.proveedor.nombre
        }
        data.append(content)
    return JsonResponse({'data': data})

def product_byid(request, id):

    if request.method == 'GET':
        try:
            product = Producto.objects.get(id=id)
            data ={
                'nombre': product.nombre,
                'precio': product.precio,
                'stock_actual': product.stock_actual,
                'proveedor': product.proveedor.nombre
            }
            return JsonResponse({'data': data})
        except Producto.DoesNotExist:
            return JsonResponse({'error': 'El producto no existe'})
        

def product_filter(request, title):
    if request.method == 'GET':
        try:
            data =[]
            products = Producto.objects.filter(nombre__contains=title)
            for items in products:
                content = {
                    'nombre': items.nombre,
                    'precio': items.precio,
                    'stock_actual': items.stock_actual,
                    'proveedor': items.proveedor.nombre
                }
                data.append(content)
            return JsonResponse({'data': data})
        except Producto.DoesNotExist:
            return JsonResponse({'error': 'El producto no existe'})
        

def proveedor_list(request):
    data = []
    proveedores = Proveedor.objects.all()
    for items in proveedores:
        content = {
            'nombre': items.nombre,
            'apellido': items.apellido,
            'dni': items.dni
        }
        data.append(content)
    return JsonResponse({'data': data})

def proveedor_byid(request, id):
    if request.method == 'GET':
        try:
            proveedor = Proveedor.objects.get(id=id)
            data = {
                'nombre': proveedor.nombre,
                'apellido': proveedor.apellido,
                'dni': proveedor.dni
            }
            return JsonResponse({'data': data})
        except Proveedor.DoesNotExist:
            return JsonResponse({'error': 'El proveedor no existe'})
        
def proveedor_filter(request, title):

    if request.method == 'GET':
        try:
            data = []
            proveedores = Proveedor.objects.filter(nombre__contains=title)
            for items in proveedores:
                content = {
                    'nombre': items.nombre,
                    'apellido': items.apellido,
                    'dni': items.dni
                }
                data.append(content)
            return JsonResponse({'data': data})
        except Proveedor.DoesNotExist:
            return JsonResponse({'error': 'El proveedor no existe'})
        
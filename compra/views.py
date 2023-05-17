from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect, JsonResponse

from compra.forms import ProductoForm, ProveedorForm
from .models import Producto, Proveedor

# Create your views here.

#create the main page view
def index(request):
    return render(request, 'index.html')


def create_product(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            data = Producto(
                nombre = form.cleaned_data['nombre'],
                precio = form.cleaned_data['precio'],
                stock_actual = form.cleaned_data['stock_actual'],
                proveedor = form.cleaned_data['proveedor']
                )
            data.save()
            return redirect('/productos/')
        else:
            return redirect('/productos/')

    context = {
        'form': form
    }
    return render(request, 'create_prod.html', context)
    

def create_proveedor(request): 
    form = ProveedorForm()
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            data = Proveedor(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                dni = form.cleaned_data['dni']
            )
            data.save()
            return redirect('/provedores/')
            
        else:
            return redirect('/provedores/')
    
    context = {
        'form': form
    }
    return render(request, 'create_prov.html', context)


def update_product(request, prod_id):
    try:

        producto = Producto.objects.get(id=prod_id)

        context = {
            'producto': producto
        }

        if request.method == 'POST':
            producto.nombre = request.POST['nombre']
            producto.precio = request.POST['precio']
            producto.stock_actual = request.POST['stock_actual']
            producto.proveedor = request.POST['proveedor']
            producto.save() # forzar un guardado en la DB siempre estar seguro de esto
        
        return render(request, 'update_prod.html', context)
    except Exception:
        return redirect('error.html')

def update_proveedor(request, prov_id):
    try:

        provedor = Proveedor.objects.get(id=prov_id)

        context ={
            'provedor': provedor
        }
        if request.method == 'POST':
            provedor.nombre = request.POST['nombre']
            provedor.apellido = request.POST['apellido']
            provedor.dni = request.POST['dni']
            provedor.save()

        return render(request, 'update_prov.html', context)
    except Exception:
        return redirect('error.html')
    


def delete_product(request, prod_id):

    try:
        producto = get_object_or_404(Producto, id=prod_id)

        if request.method == 'POST':

            producto.delete()

            return redirect('/delete/')
        
        context={
            'producto': producto
        }

        return render(request, 'delete_prod.html', context)
    
    except Exception:

        return redirect('error.html')


def delete_proveedor(request, prov_id):
        
    try:
        proveedor =Proveedor.objects.get(id=prov_id)

        if request.method == 'POST':

            proveedor.delete()

            return redirect('/delete/')
        
        context = {
            'proveedor': proveedor
        }

        return render(request, 'delete_prov.html', context)
    
    except Exception:

        return redirect('error.html')
    
    
def delete(request):
    return render(request, 'delete.html')


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
        
#lista de productos en el HTML
def productos(request):
    try:

        productos = Producto.objects.all()
        context = {
            'productos': productos,
        }
        return render(request, 'productos.html', context =context)
    except Exception:
        return render(request, 'error.html')

#lista de provedores para el HTML
def proveedores(request):
    try:
        provedor = Proveedor.objects.all()
        context = {
            'provedor': provedor
        }
        return render(request, 'proveedores.html', context=context)
    except Exception:
        return render(request, 'error.html')
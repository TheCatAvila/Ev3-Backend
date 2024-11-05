from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    # Obtener todos los productos
    listaProductos = Producto.objects.all()
    
    # Añadir el rango de estrellas a cada producto
    for producto in listaProductos:
        # Crea un rango de estrellas basado en el valor de `stars`
        producto.range_stars = range(producto.stars)  # Esto crea un rango desde 0 hasta `producto.stars`

    # Datos para el renderizado
    datos = {
        'listaProductos': listaProductos
    }

    # Renderizamos la plantilla con los datos
    return render(request, 'core/index.html', datos)

def addProducto(request):
    datos = {
        'form':ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['msj'] = "Producto Guardado correctamente"
    
    return render(request, 'core/productos/add.html', datos)

def updateProducto(request, id):
    producto = Producto.objects.get(id=id)
    datos = {
        'form':ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['msj'] = "Producto Actualizados correctamente"
            datos['form'] = formulario
    
    return render(request, 'core/productos/update.html', datos)

def deleteProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    
    return redirect(to="index")
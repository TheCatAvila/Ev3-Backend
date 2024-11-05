from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'), #PÁGINA DE INICIO
    # CRUD PRODUCTOS
    path('add-producto/', addProducto, name='addProducto'), # ADD PRODUCTOS
    path('updateProducto/<id>/', updateProducto, name='updateProducto'), # UPDATE PRODUCTOS
    path('deleteProducto/<id>/', deleteProducto, name='deleteProducto'), # DELETE PRODUCTOS
]
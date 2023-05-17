from django.urls import path
from . import views

urlpatterns = [
    #main page
    path('', views.index, name='index'),
    
    #PRODUCTOS
    path('productos/', views.productos, name='productos'),
    path("create_prod/", views.create_product, name='create-producto'),  # type: ignore
    path('update_prod/<int:prod_id>/', views.update_product, name='update-producto'),
    path('delete_prod/<int:prod_id>/', views.delete_product, name='delete-prod'),

    #PROVEEDORES
    path("provedores/", views.proveedores, name='proveedores'),
    path("create_prov/", views.create_proveedor, name="create-prov"), #type: ignore
    path("update_prov/<int:prov_id>/", views.update_proveedor, name='update-prov'),
    path('delete_prov/<int:prov_id>/', views.delete_proveedor, name="delete-prov"),

    #DELETE
    path('delete/', views.delete, name='delete-producto'),



] 

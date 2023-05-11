from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('producto/list', views.product_list),
    path('producto/<int:id>', views.product_byid), # type: ignore
    path('producto/filter/<str:title>', views.product_filter), # type: ignore
    path('proveedor/list', views.proveedor_list),
    path('proveedor/<int:id>', views.proveedor_byid), # type: ignore
    path('proveedor/filter/<str:title>', views.proveedor_filter), # type: ignore
]
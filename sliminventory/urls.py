from django.contrib import admin
from django.urls import path
from app.api.product import ProductListView, ProductDetailView
from app.api.supplier import SupplierListView, SupplierDetailView
from app.api.warehouse import WarehouseListView, WarehouseDetailView

urlpatterns = [
    path('admin/', admin.site.urls),

    # products
    path('api/products/', ProductListView.as_view()),
    path('api/products/<int:pk>/', ProductDetailView.as_view()),

    # suppliers
    path('api/suppliers/', SupplierListView.as_view()),
    path('api/suppliers/<int:pk>/', SupplierDetailView.as_view()),

    # warehouses
    path('api/warehouses/', WarehouseListView.as_view()),
    path('api/warehouses/<int:pk>/', WarehouseDetailView.as_view())
]

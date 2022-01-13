from django.contrib import admin
from django.urls import path
from app.api.product import ProductListView, ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),

    # products
    path('api/products/', ProductListView.as_view()),
    path('api/products/<int:pk>/', ProductDetailView.as_view())
]

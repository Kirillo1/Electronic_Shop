from django.urls import path

from e_shop.views.products import (IndexView, ProductDetailView)

app_name = "products"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_view"),
]

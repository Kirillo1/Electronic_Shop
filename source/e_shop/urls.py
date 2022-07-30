from django.urls import path

from e_shop.views.products import (IndexView, ProductDetailView,
                                   ProductCreateView, ProductUpdateView,
                                   ProductDeleteView)

app_name = "products"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="product_view"),
    path('product/add/', ProductCreateView.as_view(), name="product_add"),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name="product_update"),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name="product_delete"),
]

from django.urls import path

from e_shop.views.carts import (CartListView, CartDeleteView,
                                CartAddView, CartOneDelete)
from e_shop.views.orders import OrderCreateView
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
    path('carts', CartListView.as_view(), name="cart_view"),
    path('cart/<int:pk>/delete', CartDeleteView.as_view(), name="cart_delete"),
    path('cart/<int:pk>/products/add/', CartAddView.as_view(), name="cart_add"),
    path('cart/<int:pk>/delete', CartOneDelete.as_view(), name="cart_one_delete"),
    path('order/create', OrderCreateView.as_view(), name="order_create_view"),
]

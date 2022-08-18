from django.urls import reverse_lazy
from django.views.generic import CreateView

from e_shop.forms import OrderForm
from e_shop.models import (Order, ItemInCart,
                           OrderProduct, Product)


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('products:index')

    def form_valid(self, form):
        response = super().form_valid(form)
        order = self.object

        cart_products = ItemInCart.objects.all()
        products = []
        order_products = []
        for item in cart_products:
            product = item.product
            quantity = item.quantity
            product.remainder -= quantity
            products.append(product)
            order_product = OrderProduct(product=product, quantity=quantity, order=order)
            order_products.append(order_product)

        OrderProduct.objects.bulk_create(order_products)
        Product.objects.bulk_update(products, ("remainder",))
        cart_products.delete()
        return response

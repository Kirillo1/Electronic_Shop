from django.contrib import admin

from .models import (Product, ItemInCart,
                     Order, OrderProduct)

admin.site.register(Product)
admin.site.register(ItemInCart)
admin.site.register(Order)
admin.site.register(OrderProduct)

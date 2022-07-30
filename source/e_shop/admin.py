from django.contrib import admin

from .models import Product, ItemInCart

admin.site.register(Product)
admin.site.register(ItemInCart)


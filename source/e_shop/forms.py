from django import forms

from e_shop.models import Product, ItemInCart, Order


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Search")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class CartForm(forms.ModelForm):
    class Meta:
        model = ItemInCart
        fields = ["quantity"]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ["products", "user_name"]

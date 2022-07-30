from django import forms

from e_shop.models import Product, ItemInCart


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

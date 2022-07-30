from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, CreateView

from e_shop.forms import CartForm
from e_shop.models import ItemInCart, Product


class CartListView(ListView):
    template_name = 'carts/cart_list_view.html'
    model = ItemInCart
    context_object_name = 'carts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = ItemInCart.get_total()
        context['total'] = total
        return context


class CartDeleteView(DeleteView):
    model = ItemInCart
    success_url = reverse_lazy('products:cart_view')

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class CartAddView(CreateView):
    model = ItemInCart
    form_class = CartForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        quantity = form.cleaned_data.get("quantity", 1)
        try:
            cart = ItemInCart.objects.get(product=product)
            if cart.quantity + quantity <= product.remainder:
                cart.quantity += quantity
                cart.save()
        except ItemInCart.DoesNotExist:
            if quantity <= product.remainder:
                ItemInCart.objects.create(product=product, quantity=quantity)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next = self.request.GET.get("next")
        if next:
            return next
        return reverse('products:index')


class CartOneDelete(DeleteView):
    model = ItemInCart
    success_url = reverse_lazy('products:cart_view')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        self.object.quantity -= 1
        if self.object.quantity < 1:
            self.object.delete()
        else:
            self.object.save()
        return HttpResponseRedirect(success_url)

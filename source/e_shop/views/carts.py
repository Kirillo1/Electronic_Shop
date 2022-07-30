from django.views.generic import ListView

from e_shop.models import ItemInCart


class CartListView(ListView):
    template_name = 'carts/cart_list_view.html'
    model = ItemInCart
    context_object_name = 'carts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = ItemInCart.get_total()
        context['total'] = total
        return context


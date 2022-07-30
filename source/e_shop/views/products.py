from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from e_shop.forms import ProductForm
from e_shop.models import Product
from e_shop.views.base import SearchView


class IndexView(SearchView):
    model = Product
    context_object_name = 'products'
    template_name = "products/index.html"
    paginate_by = 5
    ordering = ['name', 'category']
    search_fields = ["name__icontains", "description__icontains"]

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        return queryset.order_by("name", "category").filter(remainder__gt=0)


class ProductDetailView(DetailView):
    template_name = 'products/detail.html'
    model = Product

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_name'] = "product_update.html"
    #     context['product_pk'] = self.get_object().pk
    #     return context

    def get_queryset(self):
        return super().get_queryset().filter(remainder__gt=0)


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "shop.add_product"
    model = Product
    form_class = ProductForm
    template_name = "products/create.html"

    def get_success_url(self):
        return reverse('products:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "shop.change_product"
    form_class = ProductForm
    template_name = "products/update.html"
    model = Product

    def get_success_url(self):
        return reverse('products:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "shop.delete_product"
    template_name = "products/delete.html"
    model = Product
    success_url = reverse_lazy('products:index')


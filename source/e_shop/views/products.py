from django.views.generic import DetailView

from e_shop.models import Product
from source.e_shop.views.base import SearchView


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

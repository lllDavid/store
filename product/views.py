from django.views.generic import ListView, DetailView

from .models import Product


class ProductGridView(ListView):
    model = Product
    template_name = 'product-grid.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-detail.html'
    context_object_name = 'product'



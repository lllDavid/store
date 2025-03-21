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
    # Get the stock range for dynamic quantity option in dropdown
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        context['stock_range'] = range(1, product.stock + 1)
        return context





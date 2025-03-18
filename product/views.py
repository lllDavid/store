from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Product

def home(request):
    return render(request, 'home.html')

class ProductListView(ListView):
    model = Product
    template_name = 'product-list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-detail.html'
    context_object_name = 'product'



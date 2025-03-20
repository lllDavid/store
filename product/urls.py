from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductGridView.as_view(), name='product-grid'),  
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),  
]

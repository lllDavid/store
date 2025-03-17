from django.db import models
from django.conf import settings

from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)  
    
    def __str__(self):
        return f"Cart for {self.user.email} - {self.created_at}"

    def get_total_price(self):
        """ Calculate the total price of the cart by summing the prices of each item. """
        total_price = sum(item.get_item_total() for item in self.cart_items.all())
        return total_price

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_item_total(self):
        """ Calculate the total price of this cart item (product price * quantity). """
        return self.product.price * self.quantity
from django.shortcuts import render
from .models import Cart

def cart_view(request):
    user = request.user
    if not user.is_authenticated:
        return render(request, 'cart.html', {'cart': None})  
    
    try:
        cart = Cart.objects.get(user=user, is_active=True)
    except Cart.DoesNotExist:
        cart = Cart(user=user, is_active=True)
        cart.id = None  

    return render(request, 'cart.html', {'cart': cart})
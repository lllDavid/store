from django.shortcuts import render, redirect
from .models import StoreUser  

def create_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_manager = StoreUser.objects  
        user = user_manager.create_user(email, username, password)
        return redirect('home')
    
    return render(request, 'registration/register.html')

'''
def create_superuser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_manager = StoreUser.objects  
        superuser = user_manager.create_superuser(email, username, password)
        return HttpResponse(f'Superuser {superuser.username} created successfully!')
    return render(request, 'create_superuser.html')
'''
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

# Nueva vista para redirigir la URL raíz a /home/
def index(request):
    return redirect('home')

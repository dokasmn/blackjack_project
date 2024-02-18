from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'cadastro/index.html')

def cadastro(request):
    return render(request, 'cadastro/cadastro.html')

def login(request):
    return render(request, 'cadastro/login.html')
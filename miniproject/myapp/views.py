from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def home(request):
    return render(request, 'base.html')
def inspirations(request):
    return render(request, 'body.html')

# def login_view(request):
#     form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

def index_page(request):
    return render(request, 'index.html')

def nike_page(request):
    return render(request, 'nike.html')

def adidas_page(request):
    return render(request, 'adidas.html')

def puma_page(request):
    return render(request, 'puma.html')

def converse_page(request):
    return render(request, 'converse.html')

def allpro_page(request):
    return render(request, 'allpro.html')
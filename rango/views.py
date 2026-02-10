from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request): 
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'name': "Yu Tian"}
    return render(request, 'rango/about.html', context_dict)
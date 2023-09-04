from django.shortcuts import render

# Create your views here.

# cookie


def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'tanver')
    return response

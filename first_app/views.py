from django.shortcuts import render

# Create your views here.

# cookie


def home(request):
    return render(request, 'home.html')

from django.shortcuts import render

# Create your views here.

# cookie


def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'tanver')
    return response


def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name': name})

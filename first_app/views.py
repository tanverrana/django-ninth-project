from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.

# cookie


def home(request):
    response = render(request, 'home.html')
   # response.set_cookie('name', 'tanver',max_age=10)
    response.set_cookie(
        'name', 'tanver', expires=datetime.utcnow()+timedelta(days=7))
    return response


def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name': name})


def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response

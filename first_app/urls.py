from django.urls import path
from . import views
urlpatterns = [
    # path('', views.home),
    path('', views.set_session),  # for session
    path('get_session/', views.get_session),  # for session
    path('get/', views.get_cookie, name='get_cookie'),
    path('delete/', views.delete_cookie, name='delete_cookie'),
    path('delete_session/', views.delete_session, name='delete_session')
]

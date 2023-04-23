from django.urls import path
from django.views.generic import TemplateView
from . import views 

urlpatterns = [
    path('register', views.register, name='register'), 
    path('login', views.login, name='login'), 
    path('logout', views.logout, name='logout'),
  
]
class HomePageView(TemplateView):
    template_name = 'shirdi.html'
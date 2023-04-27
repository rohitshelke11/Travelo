from django.urls import path

from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('destination/<int:id>', views.place, name='place'),
    path('destination/place/<int:id>', views.place_atual, name='place_atual')
]
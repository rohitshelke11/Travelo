from django.shortcuts import render
from .models import Destination
from .models import Place
from .models import Review
# Create your views here.

def home(request):

    dests = Destination.objects.all()


    return render(request,'index.html', {'dests': dests})


def place(request, id):

    places = Place.objects.all().filter(destination=id)
    dest = Destination.objects.get(id=id)
    
    return render(request, 'destination.html', {'places' : places,'dest' : dest, 'mapbox_access_token': 'pk.eyJ1Ijoic2FoaWxzaGFpa2gxNjM0IiwiYSI6ImNrdXV2eTVvZTFoMnIydmxuaXFia3kxYXcifQ.HALeRa9ddGCfM85eJA8GpA'})

def place_atual(request, id):

    place = Place.objects.get(id=id)
    
    review = Review.objects.all().filter(place_id=id)
    return render(request, 'place.html', {'place' : place, 'review' : review})


from django.shortcuts import render
from .models import Destination
from .models import Place
# Create your views here.

def home(request):

    dests = Destination.objects.all()


    return render(request,'index.html', {'dests': dests})


def place(request, id):

    places = Place.objects.all().filter(destination=id)
    dest = Destination.objects.get(id=id)
    print(dest.name)
    return render(request, 'destination.html', {'places' : places,'dest' : dest})

def place_atual(request, id):

    place = Place.objects.get(id=id)

    return render(request, 'place.html', {'place' : place})
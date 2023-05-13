from django.contrib import admin
from .models import Destination
from .models import Place
from .models import Review
# Register your models here.

admin.site.register(Destination)
admin.site.register(Place)
admin.site.register(Review)
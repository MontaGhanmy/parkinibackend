from django.contrib import admin
from .models import Utilisateur, Parking, Place

admin.site.register(Utilisateur)
admin.site.register(Parking)
admin.site.register(Place)


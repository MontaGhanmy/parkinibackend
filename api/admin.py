from django.contrib import admin
from .models import Utilisateur, Parking, Place, Voiture, Occupation

admin.site.register(Utilisateur)
admin.site.register(Parking)
admin.site.register(Place)
admin.site.register(Occupation)
admin.site.register(Voiture)


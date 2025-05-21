from django.contrib import admin
from .models import Enseignant, Salle, Materiel, Accessoire, Emprunt

# Register your models here.


admin.site.register(Enseignant)
admin.site.register(Salle)
admin.site.register(Materiel)
admin.site.register(Accessoire)
admin.site.register(Emprunt)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_materiel, name='liste_materiel'),
    path('ajouter_materiel/', views.ajouter_materiel, name='ajouter_materiel'),
    path('emprunt/<int:materiel_id>/', views.emprunt, name='emprunt'),
    path('salle/<int:salle_id>/', views.materiel_par_salle, name='materiel_par_salle'),
    path('enseignant/<int:enseignant_id>/', views.materiel_par_enseignant, name='materiel_par_enseignant'),
    path('historique/<int:materiel_id>/', views.historique_materiel, name='historique_materiel'),
    path('ajouter_enseignant/', views.ajouter_enseignant, name='ajouter_enseignant')
]
from django.db import models
from django.utils import timezone
import pytz

# Create your models here.
class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Salle(models.Model):
    nom = models.CharField(max_length=10)
    def __str__(self):
        return self.nom
    
class Accessoire(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

ETAT_CHOIX = [
    ('Neuf', 'Neuf'),
    ('Bon état', 'Bon état'),
    ('Usé', 'Usé'),
    ('HS', 'Hors Service')]
BUDGET_CHOIX = [
    ('Année Courante', 'Année Courante'),
    ('Projets', 'Projets'),
    ('Financements Exceptionnels', 'Financements Exceptionnels')]

TYPE_MATERIEL = [
    ('Smartphone', 'Smartphone'),
    ('Tablette', 'Tablette'),
    ('Ordinateur', 'Ordinateur'),
    ('Imprimante', 'Imprimante'),
    ('Projecteur', 'Projecteur'),
    ('Pointeur Laser', 'Pointeur Laser'),
    ('Écran', 'Écran'),
    ('Autre', 'Autre')]

class Materiel(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TYPE_MATERIEL)
    budget = models.CharField(max_length=100, choices=BUDGET_CHOIX)
    responsable = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name="materiels_responsable")
    salle = models.ForeignKey(Salle, on_delete=models.SET_NULL, null=True)
    possesseur = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name="materiels_possedes")
    accessoire = models.ForeignKey(Accessoire, on_delete=models.SET_NULL, null=True, blank=True)
    etat = models.CharField(max_length=100,  choices=ETAT_CHOIX, default="Neuf")
    def __str__(self):
        return f"{self.nom} - {self.responsable.nom if self.responsable else 'Aucun'} - {self.salle.nom if self.salle else 'Aucune'}"


class Emprunt(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    ancien_possesseur = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name="emprunts_anciens")
    nouveau_possesseur = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name="emprunts_nouveaux")
    date_emprunt = models.DateTimeField(auto_now_add=True)
    lieu = models.ForeignKey(Salle, on_delete=models.SET_NULL, null=True)
    occasion = models.CharField(max_length=100)
    objectif = models.TextField()
    def __str__(self):
        return f"{self.materiel.nom} - {self.nouveau_possesseur.nom} - {self.date_emprunt.strftime('%d-%m-%Y %H:%M')}"
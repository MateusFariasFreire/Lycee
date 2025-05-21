from django import forms
from .models import Materiel, Emprunt, Enseignant

class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = '__all__'

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['nouveau_possesseur', 'lieu', 'occasion', 'objectif']

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = '__all__'
from django.shortcuts import render, get_object_or_404, redirect
from .models import Materiel, Salle, Enseignant, Emprunt
from .forms import MaterielForm, EmpruntForm, EnseignantForm


def liste_materiel(request):
    materiels = Materiel.objects.all()
    return render(request, 'liste_materiel.html', {'materiels': materiels})


def ajouter_materiel(request):
    if request.method == "POST":
        form = MaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_materiel')
    else:
        form = MaterielForm()
    return render(request, 'ajout_materiel.html', {'form': form})


def emprunt(request, materiel_id):
    materiel = get_object_or_404(Materiel, id=materiel_id)
    if request.method == "POST":
        form = EmpruntForm(request.POST)
        if form.is_valid():
            emprunt = form.save(commit=False)
            emprunt.materiel = materiel
            emprunt.ancien_possesseur = materiel.possesseur
            materiel.possesseur = emprunt.nouveau_possesseur
            materiel.salle = emprunt.lieu
            materiel.save()
            emprunt.save()
            return redirect('liste_materiel')
    else:
        form = EmpruntForm()
    return render(request, 'emprunt.html', {'form': form, 'materiel': materiel})


def materiel_par_salle(request, salle_id):
    salle = get_object_or_404(Salle, id=salle_id)
    materiels = Materiel.objects.filter(salle=salle)
    return render(request, 'salle.html', {'salle': salle, 'materiels': materiels})


def materiel_par_enseignant(request, enseignant_id):
    enseignant = get_object_or_404(Enseignant, id=enseignant_id)
    possedes = Materiel.objects.filter(possesseur=enseignant)
    responsables = Materiel.objects.filter(responsable=enseignant)
    return render(request, 'enseignant.html', {
        'enseignant': enseignant,
        'possedes': possedes,
        'responsables': responsables
    })


def historique_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, id=materiel_id)
    emprunts = Emprunt.objects.filter(materiel=materiel).order_by('-date_emprunt')
    return render(request, 'materiel.html', {'materiel': materiel, 'emprunts': emprunts})


def ajouter_enseignant(request):
    if request.method == "POST":
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_materiel')  # Redirigez vers la page de liste après l'ajout
    else:
        form = EnseignantForm()
    return render(request, 'ajout_enseignant.html', {'form': form})
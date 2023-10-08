from django.shortcuts import render, redirect

from WebExam7.Plant.forms import CreatePlantForm, EditPlantForm, DeletePlantForm
from WebExam7.Plant.models import Plant
from WebExam7.Profile.views import get_profile


# Create your views here.
def plant_create(request):
    profile = get_profile()

    form = CreatePlantForm()
    if request.method == "POST":
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'create-plant.html', context)


def plant_details(request,  id):
    profile = get_profile()
    plant = Plant.objects.get(pk=id)

    context = {
        'profile': profile,
        'plant': plant,
    }

    return render(request, 'plant-details.html', context)


def plant_edit(request, id):
    profile = get_profile()
    plant = Plant.objects.get(pk=id)

    form = EditPlantForm(instance=plant)
    if request.method == "POST":
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'plant': plant,
        'form': form,
    }

    return render(request, 'edit-plant.html', context)


def plant_delete(request, id):
    profile = get_profile()
    plant = Plant.objects.get(pk=id)

    form = DeletePlantForm(instance=plant)
    if request.method == 'POST':
        form = DeletePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'plant': plant,
        'form': form,
    }

    return render(request, 'delete-plant.html', context)

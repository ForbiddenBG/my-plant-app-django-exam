from django.shortcuts import render, redirect

from WebExam7.Plant.models import Plant
from WebExam7.Profile.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from WebExam7.Profile.models import Profile


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


# Create your views here.
def home_page(request):
    # if get_profile() is not None:
    #     return redirect('index')

    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'home-page.html', context)


def profile_create(request):
    form = CreateProfileForm()
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def catalogue_page(request):
    profile = get_profile()
    plants = Plant.objects.all()

    context = {
        'profile': profile,
        'plants': plants,
    }

    return render(request, 'catalogue.html', context)


def profile_details(request):
    profile = get_profile()
    plants = Plant.objects.all()

    context = {
        'profile': profile,
        'plants': plants,
    }

    return render(request, 'profile-details.html', context)


def profile_edit(request):
    profile = get_profile()

    form = EditProfileForm(instance=profile)
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()

    form = DeleteProfileForm(instance=profile)
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'delete-profile.html', context)

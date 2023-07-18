from django.shortcuts import render, redirect

from petstagram.accounts.models import PetstagramUser
from petstagram.common.forms import CommentForm
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetForm, PetDeleteForm


# Create your views here.
def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet_user = request.user
        pet.save()
        form.save_m2m()
        return redirect('profile-details', pk=1)

    context = {
        'form': form
    }

    return render(request, template_name='pets/pet-add-page.html', context=context)


def show_pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    owner = PetstagramUser.objects.get(username=username)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
        'owner': owner
    }

    return render(request, template_name='pets/pet-details-page.html', context=context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)
    form = PetDeleteForm(initial=pet.__dict__)

    context = {
        'form': form,
        'pet': pet
    }

    return render(request, template_name='pets/pet-delete-page.html', context=context)


def details_pet(request, username, pet_name):
    return render(request, template_name='pets/pet-details-page.html')


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details_pet', username, pet_slug)

    context = {
        'form': form,
        'pet': pet
    }

    return render(request, template_name='pets/pet-edit-page.html', context=context)

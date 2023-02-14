from django.shortcuts import render


def register(request):
    return None


def login(request):
    return None


def show_profile_details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_profile(request):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request):
    return render(request, template_name='accounts/profile-delete-page.html')

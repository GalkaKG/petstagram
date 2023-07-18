from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from petstagram.accounts.forms import PetstagramUserCreateForm
from petstagram.accounts.models import PetstagramUser


class UserRegisterView(generic.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


def login(request):
    return None


def show_profile_details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_profile(request):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request):
    return render(request, template_name='accounts/profile-delete-page.html')

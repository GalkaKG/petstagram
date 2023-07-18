from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views

from petstagram.accounts.forms import PetstagramUserCreateForm, LoginForm
from petstagram.accounts.models import PetstagramUser


class UserRegisterView(generic.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('home')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


def show_profile_details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_profile(request):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request):
    return render(request, template_name='accounts/profile-delete-page.html')

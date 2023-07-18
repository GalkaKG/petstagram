from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from petstagram.accounts.models import PetstagramUser


class PetstagramUserCreateForm(UserCreationForm):
    class Meta:
        model = PetstagramUser
        fields = ('username', 'email')


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'Password'})
    )


class PetstagramUserEditForm(forms.ModelForm):
    class Meta:
        model = PetstagramUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'gender')
        exclude = ('password',)
        labels = {'username': 'Username',
                  'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'email': 'Email',
                  'profile_picture': 'Image',
                  'gender': 'Gender:'
                  }

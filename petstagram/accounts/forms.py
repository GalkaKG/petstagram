from django.contrib.auth.forms import UserCreationForm

from petstagram.accounts.models import PetstagramUser


class PetstagramUserCreateForm(UserCreationForm):
    class Meta:
        model = PetstagramUser
        fields = ('username', 'email')

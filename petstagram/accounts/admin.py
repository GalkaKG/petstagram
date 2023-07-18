from django.contrib import admin

from petstagram.accounts.models import PetstagramUser


@admin.register(PetstagramUser)
class PetstagramUserAdmin(admin.ModelAdmin):
    pass

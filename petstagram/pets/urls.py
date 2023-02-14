from django.urls import path, include

from petstagram.pets import views

urlpatterns = [
    path('add/', views.add_pet, name='add-pet'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', views.details_pet, name='details_pet'),
        path('edit/', views.edit_pet, name='edit_pet'),
        path('delete/', views.delete_pet, name='delete_pet'),
    ])),
]


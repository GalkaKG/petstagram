from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.UserDetailsView.as_view(), name='profile-details'),
        path('edit/', views.UserEditView.as_view(), name='profile-edit'),
        path('delete/', views.delete_profile, name='profile-delete'),
    ]))

]
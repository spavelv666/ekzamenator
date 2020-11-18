from django.urls import path
#from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path ('add/', views.UsersCreateView.as_view(), name='UsersCreateView'),
    path('usersview/', views.UsersView.as_view(), name="Users_View"),
    path("<slug:slug>/", views.UsersDetailView.as_view(), name="users_detail"),
    path('update/<int:id>/', views.UsersUpdate.as_view(), name="users_update"),
    path('delete/<int:id>/', views.UsersDelete.as_view(), name="users_delete"),
    path('accounts/login/',LoginView.as_view(), name="login"),
    path('accounts/logout/',LogoutView.as_view(), name="logout"),
  #  path('dlogout', auth_wiews.logout),
]

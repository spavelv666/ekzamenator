from django.urls import path
#from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('uchlist/', views.UchListView.as_view(), name="Uch_List"),
    path('ppview/', views.PpViewList, name="ppview"),
    path("search/", views.Search.as_view(), name='search'),
    path ('add/', views.UsersCreateView.as_view(), name='UsersCreateView'),
    path('usersview/', views.UsersView.as_view(), name="Users_View"),
    path ('uchadd/', views.UchCreateView.as_view(), name='Uch_Create'),

    path("<slug:slug>/", views.UsersDetailView.as_view(), name="users_detail"),
    path('update/<int:pk>/', views.UsersUpdate.as_view(), name="users_update"),
    path('uchupdate/<int:pk>/', views.UchUpdate.as_view(), name="uch_update"),
    path('uchdelete/<int:id>/', views.UchDelete.as_view(), name="uch_delete"),
    path('delete/<int:id>/', views.UsersDelete.as_view(), name="users_delete"),
    path('accounts/login/',LoginView.as_view(), name="login"),
    path('accounts/logout/',LogoutView.as_view(), name="logout"),
  #  path('dlogout', auth_wiews.logout),

]

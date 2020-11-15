from django.urls import path

from . import views

urlpatterns = [
    path ('add/', views.UsersCreateView.as_view(), name='UsersCreateView'),
    path('', views.UsersView.as_view()),
    path("<slug:slug>/", views.UsersDetailView.as_view(), name="users_detail")
]

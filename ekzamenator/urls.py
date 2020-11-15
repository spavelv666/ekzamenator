from django.urls import path

from . import views

urlpatterns = [
   # path("", views.UsersView.as_view()),
 #   path ('ekzamen/', ekzamen, name='ekzamen'),
# path ('add/', views.UsersCreateView.as_view(), name='add'),
   path('', views.vhod, name='vhod'),
    ]
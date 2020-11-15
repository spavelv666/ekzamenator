from django.conf import settings
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import render
from django.urls import  reverse_lazy
from  django.views.generic.edit import CreateView

from .forms import UsersForm
from  .models import Users, Pp, Uch, Shu

class UsersView(ListView):
   """Список фильмов"""
   model = Users
   queryset = Users.objects.all()
   #template_name = "ekzamenator/index.html"
   paginate_by = 2


class UsersDetailView(DetailView):
   """Полное описание фильма"""
   model = Users
   slug_field = "id"

def ekzamen(request):
   pp = Pp.objects.all()
   pp_col = Pp.objects.all().count()
   user = Users.objects.all()
   user_col = Users.objects.all().count()
   context = {'pp': pp, 'pp_col': pp_col, 'user': user, 'user_col': user_col}

   return render(request, 'ekzamenator/index.html', context)

class UsersCreateView(CreateView):
   template_name = 'ekzamenator/add_user.html'
   form_class = UsersForm
   success_url = reverse_lazy('index')

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['users'] = Users.objects.all()
      return context



def vhod(request):
   return render(request, "ekzamen/vhod.html")



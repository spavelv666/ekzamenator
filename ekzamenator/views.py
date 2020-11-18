from django.conf import settings
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import render
from django.urls import  reverse_lazy, reverse
from  django.views.generic.edit import CreateView
from  django.contrib import auth
from  django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UsersForm
from  .models import Users, Pp, Uch, Shu

class UsersView(LoginRequiredMixin, ListView):
   """Список фильмов"""
   model = Users
   queryset = Users.objects.all()
#   context = {'username': auth.get_user(request).username}
   #template_name = "ekzamenator/index.html"
   paginate_by = 2


class UsersDetailView(LoginRequiredMixin, DetailView):
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

class UsersCreateView(LoginRequiredMixin, CreateView):
   template_name = 'ekzamenator/add_user.html'
   form_class = UsersForm
   success_url = reverse_lazy("Users_View")

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['users'] = Users.objects.all()
      return context

class UsersUpdate(LoginRequiredMixin, View):
   def get(self, request, id):
      users = get_object_or_404(Users, id=id)
      bound_form = UsersForm(instance=users)
      return render(request, 'ekzamenator/update_user.html', context={'form': bound_form, 'users': users})

   def post(self, request, id):
      users = get_object_or_404(Users, id=id)
      bound_form = UsersForm(request.POST, instance=users)
      if bound_form.is_valid():
          new_user = bound_form.save()
          return redirect(new_user)

      return render(request, 'ekzamenator/update_user.html', context={'form': bound_form, 'users': users})

class UsersDelete(LoginRequiredMixin, View):
   def get(self, request, id):
      users = get_object_or_404(Users, id=id)
      return render(request, 'ekzamenator/delete_user.html', context={'users': users})

   def post(self, request, id):
      users = get_object_or_404(Users, id=id)
      users.delete()
      return redirect(reverse("Users_View"))

def vhod(request):
   return render(request, "ekzamen/vhod.html")



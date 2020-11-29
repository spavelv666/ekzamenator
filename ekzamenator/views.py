from django.conf import settings
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.base import View
from django.shortcuts import render
from django.urls import  reverse_lazy, reverse
from  django.views.generic.edit import CreateView
from  django.contrib import auth
from  django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UsersForm, UpdateForm, UchForm
from  .models import Users, Pp, Uch, Shu
from django.contrib.auth.models import User

class UchListView(LoginRequiredMixin, ListView):
   """Список фильмов"""
   model = Uch
   queryset = Uch.objects.all()
   template_name = 'ekzamenator/uch_list.html'
   paginate_by = 10

   def get_context_data(self, **kwargs):
       ppp = Pp.objects.filter(user=self.request.user)
       new_uch = Uch.objects.filter(pp=ppp[0])

       context = super(UchListView, self).get_context_data(**kwargs)
       # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
       #   pp = Pp.object.all().name
       context['Ptemp'] = ppp
       context['uch_list'] = new_uch
       return context




class UchUpdate(LoginRequiredMixin, UpdateView):
    model = Uch
   # slug_field = "pk"
    #form_class = UsersForm
    form_class = UchForm
    template_name = "ekzamenator/update_uch.html"
    success_url = reverse_lazy("Uch_List")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ppp = Pp.objects.filter(user=self.request.user)
        shus = Shu.objects.filter(pp=ppp[0])
        context['Ptemp'] = ppp
        context['users_list'] = shus
        return context


class UchCreateView(LoginRequiredMixin, CreateView):
   template_name = 'ekzamenator/add_uch.html'
   form_class = UchForm
   success_url = reverse_lazy("Uch_List")

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       ppp = Pp.objects.filter(user=self.request.user)
       shus = Shu.objects.filter(pp=ppp[0])
       context['Ptemp'] = ppp
       context['users_list'] = shus
       return context


class UchDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        uch = get_object_or_404(Uch, id=id)
        ppp = Pp.objects.filter(user=self.request.user)
        shus = Shu.objects.filter(pp=ppp[0])

        return render(request, 'ekzamenator/delete_uch.html',
                     context={'uch':uch, 'Ptemp': ppp, 'users_list': shus})

    def post(self, request, id):
        uch = get_object_or_404(Uch, id=id)
        uch.delete()
        return redirect(reverse("Uch_List"))


class UsersView(LoginRequiredMixin, ListView):
   """Список фильмов"""
   model = Users
   queryset = Users.objects.all()
  # ppp = Pp.objects.get(name="")


   paginate_by = 10

   def get_context_data(self, **kwargs):
       ppp = Pp.objects.filter(user=self.request.user)
       new_users = Users.objects.filter(pp=ppp[0])
       context = super(UsersView, self).get_context_data(**kwargs)
       # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
    #   pp = Pp.object.all().name
       context['Ptemp'] = ppp
       context['users_list'] = new_users
       return context

class UsersDetailView(LoginRequiredMixin, DetailView):
   """Полное описание фильма"""
   model = Users
   slug_field = "id"

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       ppp = Pp.objects.filter(user=self.request.user)
       shus = Shu.objects.filter(pp=ppp[0])
       context['Ptemp'] = ppp
       context['users_list'] = shus
       return context

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
      ppp = Pp.objects.filter(user=self.request.user)
      shus= Shu.objects.filter(pp=ppp[0])
      context['Ptemp'] = ppp
      context['users_list'] = shus
      return context

   def get_form_kwargs(self):
       kwargs = super(UsersCreateView, self).get_form_kwargs()
       kwargs.update({'user': self.request.user})
       return kwargs


"""
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
"""
class UsersDelete(LoginRequiredMixin, View):
   def get(self, request, id):
      users = get_object_or_404(Users, id=id)
      ppp = Pp.objects.filter(user=self.request.user)
      shus = Shu.objects.filter(pp=ppp[0])

      return render(request, 'ekzamenator/delete_user.html', context={'users': users, 'Ptemp': ppp, 'users_list': shus})

   def post(self, request, id):
      users = get_object_or_404(Users, id=id)
      users.delete()
      return redirect(reverse("Users_View"))


class UsersUpdate(LoginRequiredMixin, UpdateView):
    model = Users
   # slug_field = "pk"
    #form_class = UsersForm
    form_class = UpdateForm
    template_name = "ekzamenator/update_users.html"
    success_url = reverse_lazy("Users_View")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ppp = Pp.objects.filter(user=self.request.user)
        shus = Shu.objects.filter(pp=ppp[0])
        context['Ptemp'] = ppp
        context['users_list'] = shus
        return context

    def get_form_kwargs(self):
        kwargs = super(UsersUpdate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class Search(ListView):
    """Поиск Людей"""
    paginate_by = 3

    def get_queryset(self):
        ppp = Pp.objects.filter(user=self.request.user)
        #new_users = Users.objects.filter(pp=ppp[0])
        fusers =Users.objects.filter((Q(nomer__icontains=self.request.GET.get("q")) |
                                    Q(name__icontains=self.request.GET.get("q")))
                                         &Q(pp=ppp[0]))
        return fusers



    def get_context_data(self, *args, **kwargs):
        #  context = super(UsersView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        #   pp = Pp.object.all().name
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context

def vhod(request):
    listings = Pp.objects.all();  # order_by('-name').filter(user__icontains=request.user)

    context = {'listings': listings}
    return render(request, "ekzamen/vhod.html", context)

def PpViewList(request):
    listings = Pp.objects.filter(user=request.user)
    #names = list.listings.name
    context = {'listings': listings}
    return render(request, 'ekzamenator/pp_view.html', context)



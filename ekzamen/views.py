#from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
#from django.urls import reverse
#from .models import Article, Comment

def index(request):
   return render(request, "index.html")

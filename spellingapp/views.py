from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect, HttpResponse, request
from .models import KeyVal

def BaseView(request):
    return render(request, 'spellingapp/landing.html')

class HomeView(ListView):
    model = KeyVal
    template_name = 'spellingapp/user_home.html'
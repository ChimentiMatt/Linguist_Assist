from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect, HttpResponse, request

def BaseView(request):
    return render(request, 'spellingapp/landing.html')
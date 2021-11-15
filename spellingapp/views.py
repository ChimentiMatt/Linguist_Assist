from django.db import models
from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse, request
from .models import KeyVal

def BaseView(request):
    return render(request, 'spellingapp/landing.html')

def HomeView(request):

    # request.user is the user who is logged in
    if KeyVal.objects == True:
        spelling_list = KeyVal.objects.filter(user=request.user)
    else:
        spelling_list = ''
    context = {
        'spelling_list': spelling_list,
    }
    return render(request, 'spellingapp/user_home.html', context)


class DeleteKeyVal(DeleteView):
    model = KeyVal
    template_name = 'spellingapp/study_page.html' 


class StudyView(ListView):
    model = KeyVal
    template_name = 'spellingapp/study_page.html'
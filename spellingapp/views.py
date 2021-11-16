from django.db import models
from django.shortcuts import get_object_or_404, redirect, render, reverse
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

def learning_view(request):
    return render(request, 'spellingapp/learning.html')


def remove_key_val(request, pk):
    word_delete = get_object_or_404(KeyVal, pk=pk)
    word_delete.delete()
    return redirect('spellingapp:study_view')

def add_key_val(request):
    word = request.POST.get('word').title()
    spelling_error = request.POST.get('spelling_error').title()

    if word == '' or spelling_error == '':
        return redirect('spellingapp:study_view')  
        
    KeyVal.objects.create(
        word=word,
        spelling_error=spelling_error,
        user=request.user
    )
    return redirect('spellingapp:study_view')



def study_view(request):
    spelling_list = KeyVal.objects.filter(user=request.user)
    context = {
        'spelling_list': spelling_list,
    }

    return render(request, 'spellingapp/study_page.html', context)



from django.db import models
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import ListView, DetailView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse, request, JsonResponse
from .models import KeyVal

import json


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
    print()
    print(dir(request.META), 'here')


    # print(request.POST, 'THIS ONE')
    # spelling_error = request.data.get('spelling_error')
    # word = request.data.get('word')
    word = request.POST.get('word')
    spelling_error = request.POST.get('spelling_error')
    # print(spelling_error, 'spelling Error'

    KeyVal.objects.create(
        spelling_error=spelling_error,
        word=word,
        user=request.user
    )
    return redirect('spellingapp:study_view')



def study_view(request):
    spelling_list = KeyVal.objects.filter(user=request.user)

    context = {
        'spelling_list': spelling_list,
    }
    # print(context, 'hi')
    return render(request, 'spellingapp/study_page.html', context)





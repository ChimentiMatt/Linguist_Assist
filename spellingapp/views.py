from django.core import paginator
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.core.paginator import Paginator
# from django.views.generic import ListView, DetailView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse, request, JsonResponse

from .models import KeyVal

import json

# Notes so I can push

def BaseView(request):
    return render(request, 'spellingapp/landing.html')

def HomeView(request):
    if KeyVal.objects == True:
        spelling_list = KeyVal.objects.filter(user=request.user)
    else:
        spelling_list = ''

    context = {
        'spelling_list': spelling_list,
    }
    return render(request, 'spellingapp/user_home.html', context)



def fetch_get(request):
    # all_data = KeyVal.objects.all()
    all_data = KeyVal.objects.filter(user=request.user)
    data_list = []
    for item in all_data:
        data_list.append({
            'word': item.word,
            'spelling_error': item.spelling_error,
        })

    return JsonResponse({'items': data_list})



def learning_view(request):
    spelling_list = KeyVal.objects.filter(user=request.user)
    
    context = {
        'spelling_list': spelling_list,
    }

    return render(request, 'spellingapp/learning.html', context)


def remove_key_val(request, pk):
    word_delete = get_object_or_404(KeyVal, pk=pk)
    word_delete.delete()
    return redirect('spellingapp:study_view')


def add_key_val(request):

    word = request.POST.get('word')
    if word == '':
        return redirect('spellingapp:study_view')
    else:
        spelling_error = request.POST.get('spelling_error')

        KeyVal.objects.create(
            spelling_error=spelling_error,
            word=word,
            user=request.user
        )

        return redirect('spellingapp:study_view')
    

def learning_add_key_val(request):
    keyVal_data = json.loads(request.body)
    word = keyVal_data['word']
    spelling_error = keyVal_data['spelling_error']
    user=request.user
    newKeyVal = KeyVal(word=word, spelling_error=spelling_error, user=user)
    newKeyVal.save()
    return HttpResponse('ok')

    

def study_view(request):
    spelling_list = KeyVal.objects.filter(user=request.user)
    paginator = Paginator(spelling_list, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'spelling_list': page_obj,
    }
    # print(context, 'hi')
    return render(request, 'spellingapp/study_page.html', context )





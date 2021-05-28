from django.shortcuts import render, redirect #redirect is new
from django.http import HttpResponse 

from .models import *
from .forms import * # this is new

def index(request):
    #return HttpResponse('sup bitches?')
    tasks = Task.objects.all()

    form = TaskForm()#this is new
    #for POST methods
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form} #add the form section
    return render(request, 'tasks/list.html', context)
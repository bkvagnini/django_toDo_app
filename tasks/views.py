from django.shortcuts import render, redirect #redirect is new
from django.http import HttpResponse 

from .models import *
from .forms import * # this is new

def index(request):
    #return HttpResponse('sup bitches?')
    tasks = Task.objects.all()

    form = TaskForm()#this is new - https://docs.djangoproject.com/en/3.2/topics/forms/
    #for POST methods
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form} #add the form section
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm (instance = task) #the instance = task refers to the task variable 2 lines above (this is how it gets the ID number)
    #this section is new
    if request.method == 'POST':
        form = TaskForm (request.POST, instance = task)
        if form.is_valid():    
            form.save()
        return redirect('/')
    #end new section
    context = {'form':form}

    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    #this section is new
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    #end new section
    context = {'item':item}
    return render(request, 'tasks/delete.html', context)




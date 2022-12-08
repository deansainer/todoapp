from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'todoapp/todolist.html', context={'tasks': tasks, 'form': form})


def deleteTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')

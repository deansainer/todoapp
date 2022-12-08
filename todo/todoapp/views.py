from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    tasks = Task.objects.all()
    return render(request, 'todoapp/todolist.html', context={'tasks': tasks})


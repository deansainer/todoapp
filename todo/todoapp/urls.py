from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='todo_list_url')
]
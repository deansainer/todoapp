from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='todo_list_url'),
    path('delete_task/<str:task_id>/', views.deleteTask, name='delete_task_url'),



]

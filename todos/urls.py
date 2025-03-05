from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo-lists/', views.todo_list_view, name='todo_list'),
    path('todo-lists/add/', views.todo_list_add, name='todo_list_add'),
    path('todo-lists/<int:pk>/', views.todo_list_detail, name='todo_list_detail'),
    path('todo-lists/<int:pk>/delete/', views.todo_list_delete, name='todo_list_delete'),
    path('todo-lists/<int:pk>/edit/', views.todo_list_edit, name='todo_list_edit'),
    path('todos/<int:pk>/delete/', views.todo_delete, name='todo_delete'),
    path('todos/<int:pk>/edit/', views.todo_edit, name='todo_edit'),
]



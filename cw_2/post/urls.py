from django.urls import path
from .views import post_list, post_detail, post_create, post_delete

urlpatterns = [
    path('', post_list, name='home'),  # Сделает / главной страницей
    path('posts/', post_list, name='post_list'),
    path('posts/<int:id>/', post_detail, name='post_detail'),
    path('posts/new/', post_create, name='post_create'),
    path('posts/<int:id>/delete/', post_delete, name='post_delete'),
]

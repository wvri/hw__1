from django.urls import path
from .views import TableListCreateView, available_tables

urlpatterns = [
    path('', TableListCreateView.as_view(), name='table-list-create'),
    path('available/', available_tables, name='available-tables'),
]

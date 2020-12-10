from django.urls import path
from app.views.create import destination_create
from app.views.delete import destination_delete
from app.views.details import destination_details
from app.views.edit import destination_edit
from app.views.index import index
from app.views.list import destination_list

urlpatterns = [
    path('', index, name='index'),
    path('list/', destination_list, name='destination list'),
    path('details/<int:pk>/', destination_details, name='destination details'),
    path('edit/<int:pk>/', destination_edit, name='destination edit'),
    path('delete/<int:pk>/', destination_delete, name='destination delete'),
    path('create/', destination_create, name='destination create'),

]

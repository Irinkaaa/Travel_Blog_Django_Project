from django.urls import path
from travel_app.views import index, destination_list, destination_details, destination_edit, destination_delete, destination_create

urlpatterns = [
    path('', index, name='index'),
    path('list/', destination_list, name='destination list'),
    path('details/<int:pk>/', destination_details, name='destination details'),
    path('edit/<int:pk>/', destination_edit, name='destination edit'),
    path('delete/<int:pk>/', destination_delete, name='destination_ delete'),
    path('create/', destination_create, name='destination create'),

]

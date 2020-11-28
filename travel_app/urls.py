from django.urls import path
from travel_app.views import index

urlpatterns = [
    path('', index, name='index')
]

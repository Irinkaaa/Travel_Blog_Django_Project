from django.shortcuts import render
from travel_app.models import Destination


def index(request):
    context = {
        'destinations': Destination.objects.all(),
    }
    return render(request, 'index.html', context)


def destination_details(request):
    pass


def destination_create(request):
    pass


def destination_edit(request):
    pass


def destination_delete(request):
    pass

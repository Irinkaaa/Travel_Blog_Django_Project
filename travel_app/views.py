from django.shortcuts import render
from travel_app.models import Destination


def index(request):
    return render(request, 'index.html')


def destination_list(request):
    context = {
        'destinations': Destination.objects.all(),
    }
    return render(request, 'destination_list.html', context)


def destination_details(request, pk):
    pass


def destination_create(request):
    pass


def destination_edit(request):
    pass


def destination_delete(request):
    pass

from django.shortcuts import render
from travel_app.models import Destinations


def index(request):
    context = {
        'destinations': Destinations.objects.all(),
    }
    return render(request, 'index.html', context)

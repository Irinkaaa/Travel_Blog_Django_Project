from django.shortcuts import render
from app.models import Destination


def destination_list(request):
    context = {
        'destinations': Destination.objects.all(),
    }
    return render(request, 'app/destination_list.html', context)

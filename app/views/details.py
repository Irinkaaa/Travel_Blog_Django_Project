from django.shortcuts import render
from django.views.decorators.http import require_GET
from app.forms.create import DestinationFrom
from app.models import Destination


@require_GET
def destination_details(request, pk):
    destination = Destination.objects.get(pk=pk)
    destination.can_delete = destination.user_id == request.user.id
    context = {
        'destination': destination,
        'form': DestinationFrom(instance=destination),
    }
    return render(request, 'app/destination_details.html', context)

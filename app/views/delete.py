from django.shortcuts import render, redirect
from app.forms.delete import DeleteDestinationForm
from app.models import Destination


def destination_delete(request, pk):
    destination = Destination.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'destination': destination,
            'form': DeleteDestinationForm(instance=destination),
        }
        return render(request, 'app/destination_delete.html', context)
    else:
        destination.delete()
        return redirect('index')

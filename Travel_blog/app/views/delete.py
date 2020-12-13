from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Travel_blog.app.forms.delete import DeleteDestinationForm
from Travel_blog.app.models import Destination


@login_required
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
        return redirect('destination list')

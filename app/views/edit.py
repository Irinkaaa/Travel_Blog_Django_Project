from django.shortcuts import render, redirect
from app.forms.edit import EditDestinationForm
from app.models import Destination


def destination_edit(request, pk):
    destination = Destination.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'destination': destination,
            'form': EditDestinationForm(instance=destination),
        }
        return render(request, 'app/destination_edit.html', context)
    else:
        form = EditDestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('destination details', destination.pk)
        else:
            context = {
                'destination': destination,
                'form': form,
            }
            return render(request, 'app/destination_edit.html', context)

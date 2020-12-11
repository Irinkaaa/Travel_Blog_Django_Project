from django.shortcuts import render, redirect
from Travel_blog.cleanup import clean_up_files
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
        old_image = destination.image
        form = EditDestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            clean_up_files(old_image.path)
            form.save()
            return redirect('destination details', destination.pk)
        else:
            context = {
                'destination': destination,
                'form': form,
            }
            return render(request, 'app/destination_edit.html', context)

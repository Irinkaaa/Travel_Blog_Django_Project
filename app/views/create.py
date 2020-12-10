from django.shortcuts import render, redirect
from app.forms.create import DestinationFrom


def destination_create(request):
    if request.method == 'GET':
        context = {
            'form': DestinationFrom(),
        }
        return render(request, 'app/destination_create.html', context)
    else:
        form = DestinationFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('destination list')
        context = {
            'form': form,
        }
        return render(request, 'app/destination_create.html', context)

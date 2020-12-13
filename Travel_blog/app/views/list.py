from django.shortcuts import render
from Travel_blog.app.models import Destination


def destination_list(request):
    destinations = Destination.objects.all()
    for dest in destinations:
        dest.can_delete = dest.user_id == request.user.id
    context = {
        'destinations': destinations,
    }
    return render(request, 'app/destination_list.html', context)

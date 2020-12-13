from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from Travel_blog.app.models import Like, Destination


def destination_likes(request, pk):
    like = Like.objects.filter(user_id=request.user.id, destination_id=pk).first()
    if like:
        like.delete()
    else:
        destination = Destination.objects.get(pk=pk)
        like = Like(field=str(pk), user=request.user)
        like.destination = destination
        like.save()
    return redirect('destination details', pk)

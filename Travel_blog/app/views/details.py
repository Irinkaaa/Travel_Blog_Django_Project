from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Travel_blog.app.forms.comment import CommentForm
from Travel_blog.app.forms.create import DestinationFrom
from Travel_blog.app.models import Destination, Comment


@login_required
def destination_details(request, pk):
    destination = Destination.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'destination': destination,
            'form': DestinationFrom,
            'comment_form': CommentForm,
            'can_delete': destination.user_id == request.user.id,
            'can_comment': destination.user_id != request.user.id,
            'can_like': destination.user_id != request.user.id,
            'has_likes': destination.like_set.filter(user_id=request.user.id).exists(),
        }
        return render(request, 'app/destination_details.html', context)

    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(comment=form.cleaned_data['comment'])
            comment.destination = destination
            comment.user = request.user
            comment.save()
            destination.comment_set.add(comment)

            return redirect('destination details', pk)

        context = {
            'destination': destination,
            'form': form
        }
        return render(request, 'app/destination_details.html', context)

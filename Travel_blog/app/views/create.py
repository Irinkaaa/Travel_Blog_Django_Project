from Travel_blog.app.forms.create import DestinationFrom
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Travel_blog.app.models import Destination


# def destination_create(request):
#     if request.method == 'GET':
#         context = {
#             'form': DestinationFrom(),
#         }
#         return render(request, 'app/destination_create.html', context)
#     else:
#         form = DestinationFrom(request.POST, request.FILES)
#         form.instance.user = request.user
#         if form.is_valid():
#             form.save()
#             return redirect('destination list')
#         context = {
#             'form': form,
#         }
#         return render(request, 'app/destination_create.html', context)


class CreateDestinationView(LoginRequiredMixin, CreateView):
    template_name = 'app/destination_create.html'
    model = Destination
    form_class = DestinationFrom

    def get_success_url(self):
        url = reverse_lazy('destination details', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        destination = form.save(commit=False)
        destination.user = self.request.user
        destination.save()
        return super().form_valid(form)

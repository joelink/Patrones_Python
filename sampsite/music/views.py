
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Album
from .forms import Userform

class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

class AlbumCreate(CreateView):
    model=Album
    fields =['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DetailView):
    model = Album
    succes_url = reverse_lazy('index')

class UserformView(View):
    form_class = Userform
    template_name = 'music/registration_form.html'
    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            #Creates user but does not save it
            user = form.save(commit=False)

            #Clenaed (normalized) data
            username = form.cleaned_data['username']
            passworld = form.cleaned_data['passworld']
            user.ser_password(passworld)
            user.save()

            # Return user objects if credentials are correct
            user = authenticate(username=username, passworld=passworld)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
        return render(request, self.template_name, {'form' : form})


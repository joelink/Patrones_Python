from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Album

# Create your views here.

def index(request):
          return HttpResponse("<h1>This is the New Music app home page </h1>")

def details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {'album': album,})

def list(request):
    all_Albums = Album.objects.all()
    # Se puede crear el diccionario con una variable como en este caso o
    # simplemtene como es solo y objeto entonces llamarlo en el return
    context = {'all_Albums': all_Albums,}
    return render(request, 'music/Album_list.html', context)
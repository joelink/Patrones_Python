from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

# Create your views here.

def index(request):
          return HttpResponse("<h1>This is the Music app home page </h1>")

def details(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not existe")
    return render(request, 'music/details.html', {'album': album,})

def list(request):
    all_Albums = Album.objects.all()
    # Se puede crear el diccionario con una variable como en este caso o
    # simplemtene como es solo y objeto entonces llamarlo en el return
    context = {'all_Albums': all_Albums,}
    return render(request, 'music/Album_list.html', context)

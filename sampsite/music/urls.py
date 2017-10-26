from django.conf.urls import url, include

from . import views

app_name = 'music'

urlpatterns = [
    #/music/
    url(r'^$', views.IndexView.as_view(), name='index'),
   # url(r'^songs/$', views.SongsView.as_view(), name='songs_index'),

    #Ingreso
   # url(r'^login_user/$', views.login_user, name='login_user'),


    #Registro
    url(r'^CreateAccount/$', views.UserformView.as_view(), name='CreateAccount'),

    # music/71/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(),name='detail'),

  #  url(r'^(?P<pk>[0-9]+)/songs/$', views.DetailViewSongs.as_view(),name='detail_song'),
    # url(r'^(?P<pk>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),

    #/music/album/add/
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'^album/details/add$', views.SongCreate.as_view(), name='song-add'),
    # /music/album/2/
    url(r'^album/add/$', views.AlbumUpdate.as_view(), name='album-update'),
    # /music/album/2/delete
    url(r'^(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

]
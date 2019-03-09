from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404 #this will either give object or 404 error it basically works live try catch
from .models import Album,Song
# Create your views here.



def index(request): # we always pass in a request

#making clickable links for albums

    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html') #loads the template from templates folder here path starts from music coz django knows we have made a templates folder
    #context is dictionary info the html needs to work
    context = {
        'all_albums': all_albums,
    }

    return HttpResponse(template.render(context, request))


def details(request, album_id):
    '''try to find the primary key which user requested in DB and if pk did not match album_id which user requested
        then raise the 404 exception'''

    album = get_object_or_404(Album, pk = album_id)
    context = {
        'album': album,
    }

    #album in context dict and get_obj_404 are same.
    #render method is compact form to load the template and give its http response
    return render(request, 'music/details.html', context)

def favorite(request, album_id):
    album = get_object_or_404(Album, pk = album_id)
    context = {'album':album}
    try:
        selected_song = album.song_set.get(pk = request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html',{'album':album,
                                                     'error_message':"You did not select valid song"})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/details.html', context)

    
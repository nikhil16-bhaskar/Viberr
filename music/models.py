from django.db import models

# Create your models here.

class Album(models.Model): #always all the classes are inherited with models.Model
    artist = models.CharField(max_length= 250) #CharField is just text or characters and max_length is max charaters it can have
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    '''this is a string dunder(double underscores) function which will show the info about objects of 
        album class in django shell while populating database. '''
    '''basically __str__ func. displays the string info of a class.'''
    def __str__(self):
        return self.artist + ' - ' + self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE) #every song is from an album so we are linking songs to album via foreign key coz album will have a primary key which will be auto generated.
    # on_delete=models.CASCADE is telling that when the album gets deleted, delete all its song from this table.

    song_title = models.CharField(max_length=500)
    file_type = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default = False)

    def __str__(self):
        return self.song_title


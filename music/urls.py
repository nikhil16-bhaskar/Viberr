from django.conf.urls import url
from . import views #importing views from same directory(.)


app_name = 'music' #this is called Namespace used to distinguish names of urls(if they are same)
                   #eg: if we have 2 apps music and videos and both have details html page then on which regex which template will be executed so it is distinguished by Namespace.

urlpatterns = [
    # regex starts at ^ and ends at $
    #this maps url /music/
    url(r'^$', views.index, name='index'), #this regex r'^$' means that user has just requested music/ and nothing else.

    #this maps url /music/21/
    #<album_id> is the variable in which the pattern of regex is stored, brackets are so that 21 is read as 21 an not 2 and 1
    # [0-9] means any digit b/w 0 to 9 and + means it will read id character by character
   url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),

    #to mark the song is favourite or not(it will not redirect to another page, its only logic to make a song fav)
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name = 'favorite'),
]
from django.conf.urls import url
from . import views #importing views from same directory(.)


app_name = 'music' #this is called Namespace used to distinguish names of urls(if they are same)
                   #eg: if we have 2 apps music and videos and both have details html page then on which regex which template will be executed so it is distinguished by Namespace.

urlpatterns = [
    # regex starts at ^ and ends at $
    #this maps url /music/
    #as_view() functions converts classes to views
    url(r'^$', views.IndexView.as_view(), name='index'), #this regex r'^$' means that user has just requested music/ and nothing else.

    #this maps url /music/21/
    #<pk> is the primary key in which the class of details view expects, brackets are so that 21 is read as 21 an not 2 and 1
    # [0-9] means any digit b/w 0 to 9 and + means it will read id character by character

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),

    #/music/album/add
    url(r'^album/add/$',views.AlbumCreate.as_view(), name='album-add'),

    #/music/album/pk/
    url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),

    #music/album/pk/delete
    #url(r'^album/(?P<pk>[0-9]+)/delete/$',views.DeleteView.as_view(),name='album-delete')

    url(r'^register/$', views.UserFormView.as_view(), name='register')



]
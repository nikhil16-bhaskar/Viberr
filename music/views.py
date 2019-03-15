from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Album
from .forms import UserForm


class IndexView(generic.ListView): #inheriting the generic list view, there are other generic views here we are using list
    template_name = 'music/index.html' #template name to which this class plugins
    context_object_name = 'all_albums' #context object name is the fixed variable name,it is used to change name of object_list to any name you want like here all albums

    def get_queryset(self): #queries database for all objects in album and returns object_list
        return Album.objects.all()


class DetailView(generic.DetailView): #using the generic detail view
    model = Album #which model we are refering
    template_name = 'music/details.html'


class AlbumCreate(CreateView): #now you want to create a view
    model = Album #what type of object will new view have? ans-Album, oh so we we are making a new album
    fields = ['artist', 'album_title', 'genre', 'album_logo'] #what fields will the new album have/we want to show.


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']



#class AlbumDelete(DeleteView):
 #   model = Album
  #  success_url = reverse_lazy('music:index') #when we will delete  any view so it will take us to index.html
    #success_url is used when we successfully delete something.

class UserFormView(View):
    form_class = UserForm #blueprint from where we will take our form
    template_name = 'music/registration_form.html' #html file associated with form_class

    #display a blank form to user
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})



    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid(): #this will check the basic validation, is_valid does the basic validation of our form
            user = form.save(commit=False) #form is saved to an object user but not to database

            #cleaned normalized data so that every one has uniform pattern

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password) #hash value password is stored in DB and not plain text,if plain text is stored ot will throw errors

            user.save() #saved to database

            user = authenticate(username = username, password =password) #authenticate the user if he./she is in DB(already registered)

            if user is not None: #if user is there
                if user.is_active: #and if user is active i.e his account is not disabled or banned by website company.
                    login(request,user) #user is permitted to login(session is given to him/her)
                    return redirect('music:index') #after login he/she is redirected to home page

        return render(request,self.template_name,{'form':form}) #if user is not in DB he is given blank form






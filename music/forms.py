from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) #to give password the asterik look (*)

    class Meta:
        model = User
        fields = ['username','email','password'] #fields which we will be using for form and this will be added to database
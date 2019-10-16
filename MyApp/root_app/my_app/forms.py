from django import forms
from django.contrib.auth.models import User
from .models import UserRegisterInfo


class UserRegisterForm(forms.ModelForm):
    ## the create the box input password
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    ##reference the form to model
    class Meta():
        ##point the base class of user model 
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
           
        } 
        fields = ('username', 'password')

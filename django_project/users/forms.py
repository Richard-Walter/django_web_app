''' This creates a custom form that inherits from
 the defaults form so we can have a email address element '''

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # gives us a nested namespace for configurations and keeps them in the one plce
    class Meta:
        model = User    # model affected
        fields = ['username', 'email', 'password1', 'password2']    # field we want in order
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import Post

# class ProfileAdmin(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['full_name', 'about', 'img']

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'image']

class signUp(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class LoginForm(AuthenticationForm):
    username = UsernameField()
    # password = forms.CharField(attrs=)  
    password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password'}))          


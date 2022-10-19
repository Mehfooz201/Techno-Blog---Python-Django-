from ast import Return
import re
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from urllib3 import Retry
from .models import Post
from .forms import postForm, signUp, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group


# Create your views here.

def home(request):
    posts = Post.objects.all()
    user = request.user 
    # full_name = user.get_full_name()
    gps = user.groups.all()
    return render(request, 'myapp/home.html', {'posts':posts, 'user':request.user, 'groups':gps})


def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def user_signup(request):
    if request.method == 'POST':
        form = signUp(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            messages.success(request, 'Congratulations, You have become an Author !')
    else:
        form = signUp()
    return render(request, 'myapp/signup.html', {'form':form})


def user_signin(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return redirect('login')                  
    else:
        form = LoginForm()     

    return render(request, 'myapp/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


# def userProfile(request):
#     if request.method == 'POST':
#         form = ProfileAdmin(request.POST, request.FILES)
#         if form.is_valid():
#             fn = form.cleaned_data['full_name']
#             ab = form.cleaned_data['about']
#             im = form.cleaned_data['img']

#             pst = Profile(full_name=fn, about=ab, img=im)
#             pst.save()
#             form = ProfileAdmin()

#             messages.success(request, 'Your Profile has been updated !')

#     else:
#         form = ProfileAdmin()
#     return render(request, 'myapp/userprofile.html', {'form':form})


def dashboard(request):
    posts = Post.objects.all()
    user = request.user 
    full_name = user.get_full_name()
    gps = user.groups.all()
    return render(request, 'myapp/dashboard.html', {'posts':posts, 'user':request.user, 'fname':full_name,'groups':gps})

def blogPost(request, post_id):
    posts = Post.objects.get(pk=post_id)
    user = request.user 
    # full_name = request.user.get_full_name() 
    # full_name = user.get_full_name()
    gps = user.groups.all()
    return render(request, 'myapp/blog.html', {'posts':posts, 'user':request.user, 'groups':gps})


def addPost(request):
    if request.method == 'POST':
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            ti = form.cleaned_data['title']
            cont = form.cleaned_data['content']
            sl = form.cleaned_data['slug']
            img = form.cleaned_data['image']

            pst = Post(title=ti, content=cont, slug=sl, image=img)
            pst.save()
            form = postForm()

            messages.success(request, 'You Post has been added !')

    else:
        form = postForm()

    return render(request, 'myapp/addpost.html', {'form':form})

def delPost(request, post_id):
    if request.method == 'POST':
        posts = Post.objects.get(pk=post_id)
        posts.delete()
    
    return redirect('dashboard')



def updatePost(request, post_id):
    if request.method == 'POST':
        upd = Post.objects.get(pk=post_id)
        form = postForm(request.POST, request.FILES, instance=upd)
        if form.is_valid():
                form.save()
                messages.success(request, 'Your Post has been updated !')
    else:
        upd = Post.objects.get(pk=post_id)
        form = postForm(instance=upd)
    
    return render(request, 'myapp/updatepost.html', {'form': form})



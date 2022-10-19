"""MehfoozBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('froala_editor/',include('froala_editor.urls')),
    path('', views.home, name='home'),
    path('/about', views.about, name='about'),
    path('/contact', views.contact, name='contact'),

    path('/dashboard', views.dashboard, name='dashboard'),
    path('/blog/<int:post_id>', views.blogPost, name='blog'),
    path('/addnewpost', views.addPost, name='addnewpost'),
    path('/delete/<int:post_id>', views.delPost, name='delete'),
    path('/updatepost/<int:post_id>', views.updatePost, name='update'),

    #login and Signup Page
    path('/register', views.user_signup, name='register'),
    path('/login', views.user_signin, name='login'),
    path('logout/', views.user_logout, name='logout'),

    #User profile
    # path('/userprofile/', views.userProfile, name='profile'),
    # path('/base/<str:username>', views.base, name='base'),


    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)
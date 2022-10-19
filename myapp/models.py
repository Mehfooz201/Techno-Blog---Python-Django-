from statistics import mode
from django.db import models
from froala_editor.fields import FroalaField
from distutils.command.upload import upload

# Create your models here.

# class Profile(models.Model):
#     profile_id = models.AutoField(primary_key=True)
#     full_name = models.CharField(max_length=100)
#     about = models.CharField(max_length=250)
#     img = models.ImageField(upload_to = 'profile')

#     def __str__(self):
#         return self.full_name
    
#     @property
#     def imageURL(self):
#         try:
#             url = self.img.url
#         except:
#             url=''
#         return url

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    # content = FroalaField()
    content = models.TextField()
    slug = models.SlugField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to = 'blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url
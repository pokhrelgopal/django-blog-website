import uuid
from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    author = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True,blank=True)
    featured_image = models.ImageField(null=True,blank=True,default="defaultBlog.png")
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title
    

from sre_parse import CATEGORIES
from django.db import models



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class contactMessage(models.Model):
     name=models.CharField(max_length=100, default='')
     email=models.CharField(max_length=100, default='')
     subject=models.CharField(max_length=500, default='')
     message=models.TextField(max_length=500, default='')
     def __str__(self):
            return f"{self.name}"
     
class blogAuthor(models.Model):
    name=models.CharField(max_length=100, default='')
    description=models.TextField(max_length=500, default='')
    image=models.ImageField(upload_to='images/author',default='')
    instagram_id=models.TextField(max_length=90, default='')
    twitter_id=models.TextField(max_length=90, default='')
    def __str__(self):
        return f"{self.name}"
     
     
     
     
class blogItem(models.Model):
    name=models.CharField(max_length=100, default='')
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    description=models.TextField(max_length=500, default='')
    image=models.ImageField(upload_to='images',default='')
    author=models.ForeignKey(blogAuthor, on_delete=models.SET_NULL, null=True)
    like = models.IntegerField(default=0)
    commentcount= models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name},{self.date}"
    
class commentItem(models.Model):
    name=models.CharField(max_length=100, default='')
    comment=models.CharField(max_length=500, default='')
    date = models.DateTimeField(auto_now_add=True)
    email=models.CharField(max_length=100, default='')
    image=models.CharField(max_length=100, default='')
    blog=models.ForeignKey(blogItem,on_delete=models.CASCADE,related_name='comments')
    def __str__(self):
        return f"{'name :'}{self.name}{'_____'}{'post name :'}{self.blog}"
    
    
    
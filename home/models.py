from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# this is home page main course table
class subject(models.Model):
    course = models.CharField(max_length=40)
    slug = models.SlugField(unique=True)
    
    def __str__(self) -> str:
        return self.course

class chapter(models.Model):
    Auth = models.CharField(max_length=255)
    Subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='img/')
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    Content = RichTextField(blank=True,null=True)
    
    def __str__(self) -> str:
        return 'data of ' + self.title

# this is cheetsheet Table
class cheetsheet(models.Model):
    Auth = models.CharField(max_length=255)
    Subject = models.CharField(max_length=50)
    image = models.ImageField(upload_to ='img/')
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=130)
    Content = RichTextField(blank=True,null=True)
    
    def __str__(self) -> str:
        return 'data of ' + self.title

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=40)
    content = models.TextField()
    time =models.DateTimeField(auto_now=True,blank=True)


    def __str__(self) -> str:
        return 'data of ' + self.name +'-'+ self.email
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User,on_delete=models.CASCADE,null=True
    )
    name = models.CharField(max_length=100,default="Boy")
    email = models.EmailField(max_length=100,default="aryanraj3041@gmail.com")
    user_name = models.CharField(max_length=100,default="user")
    headlines = models.CharField(max_length=1000,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    location = models.CharField(max_length=1000,null=True,blank=True)
    Profile_image = models.ImageField(default='profile/boy.JPG',upload_to='profile')
    social_twitter = models.CharField(max_length=100,null=True,blank=True)
    social_github = models.CharField(max_length=100,null=True,blank=True)
    social_linkedin = models.CharField(max_length=100,null=True,blank=True)
    social_website = models.CharField(max_length=100,null=True,blank=True)
    skills = models.CharField(max_length=100,default="no skillset")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class Skill(models.Model):
    owner = models.ForeignKey(Profile,on_delete= models.CASCADE,null=True,blank = True)
    name = models.CharField(max_length=100,default="")
    description = models.TextField(null=True,blank = True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,related_name='sender')
    recipient = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,related_name='reciever')
    name = models.CharField(max_length=100,default="")
    email = models.EmailField(max_length=100,default="aryanraj3041@gmail.com")
    subject = models.CharField(max_length=1000,default="no subject")
    body = models.TextField(null=True,blank=True)
    is_read = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject






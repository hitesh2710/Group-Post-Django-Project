from django.db import models
from django.contrib.auth.models import Group, User
from django.http import request
from django.urls import reverse
from datetime import datetime 


class SignUp(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('signlog:success')


class Groups(models.Model):
    name = models.CharField(max_length=256)
    desc = models.TextField()
    cjoin = models.IntegerField(default=0)
    tf = models.BooleanField(default=False)
    cpost=models.IntegerField(default=0)
    usrname=models.CharField(max_length=256,default=',')
    usrrname=models.CharField(max_length=256,default=',')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('signlog:detail', kwargs={'pk': self.pk})

    def cpostsave(self):
        self.cpost=self.cpost+1
        self.save()  
          
    def cpostsave1(self):
        self.cpost=self.cpost-1
        self.save()   


class Post(models.Model):
    Message = models.CharField(max_length=256)
    Group = models.ForeignKey(Groups, related_name='posts',on_delete=models.CASCADE)
    created_by= models.CharField(max_length=100,default=",")
    dt=models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        ordering = ('-dt',)
    
    
    
     
    def __str__(self):
        return self.Group.name

    def get_absolute_url(self):
        return reverse('signlog:postcount',kwargs={'pk':self.pk})
        
    

from django.db import models
from django.utils import timezone

# Create your models here.

class About(models.Model) :
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='posts/')
    

    def __str__(self):
        return self.title


class Skill(models.Model) :
    name = models.CharField(max_length=100)
    number = models.IntegerField(default='')
     


    def __str__(self):
        return self.name


class Experience(models.Model) :
    title = models.CharField(max_length=100)
    datefrom = models.DateField(default=timezone.now)
    dateto = models.DateField(default=timezone.now)
    description = models.TextField(max_length=2000)


    def __str__(self):
        return self.title

class Link(models.Model) :
    url= models.URLField(default='')
    icon= models.CharField(max_length=100)


    def __str__(self):
        return self.url






      

from django.db import models


# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length=100)
    name =  models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/')
    description = models.TextField(max_length=2000)
 

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class testimonial(models.Model) :
     name = models.CharField(max_length=100)
     jobname = models.CharField(max_length=120)
     image = models.ImageField(upload_to='posts/')
     Comment = models.TextField(max_length=2000)


     def __str__(self):
        return  self.name 


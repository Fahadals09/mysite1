from django.db import models

# Create your models here.
class Home(models.Model) :
    backgroundimage = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)


    def __str__(self):
        return self.title
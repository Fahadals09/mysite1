from django.db import models

# Create your models here.
class portfolio(models.Model) :
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/')


    def __str__(self):
        return self.title
    
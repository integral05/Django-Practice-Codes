from django.db import models

# Create your models here.

class Movie(models.Model):
    rdate = models.DateField(verbose_name='Release Date')
    moviename = models.CharField(max_length=30,verbose_name='Movie')
    hero = models.CharField(max_length=30,verbose_name='Hero Name')
    heroine = models.CharField(max_length=30,verbose_name="Heroine Name")
    rating = models.IntegerField(verbose_name='Rating')
    




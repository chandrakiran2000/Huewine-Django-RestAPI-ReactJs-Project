from django.db import models

# Create your models here.
class Moviesdata(models.Model):
    def __str__(self) :
        return self.moviename
    id = models.AutoField(primary_key=True)
    moviename = models.CharField(max_length=100)
    heroname= models.CharField(max_length=100)
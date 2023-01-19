from django.db import models

# Create your models here.

class Actors(models.Model):
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    bio=models.CharField(max_length=500)
    # id=models.AutoField(primary_key=True)
    def __str__(self):
        return self.name




class Producer(models.Model):
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    bio=models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Movies(models.Model):
    movie=models.CharField(max_length=200, unique=True)
    year_of_release=models.CharField(max_length=4)
    plot=models.CharField(max_length=2000)
    producer=models.ForeignKey(Producer,on_delete=models.SET_NULL,null=True,blank=True)
 
    actor=models.ManyToManyField(Actors,blank=True)
    
    def actors(self):
        return ",".join([str(p.name) for p in self.actor.all()])
    
    def __str__(self):
        return self.movie

 

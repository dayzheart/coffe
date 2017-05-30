from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Been(models.Model):
    name = models.CharField(max_length= 50)


    def __str__(self):
        return self.name


class Roast(models.Model):
    name= models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Syrup(models.Model):
    name = models.CharField(max_length= 50)


    def __str__(self):
        return self.name


class Powder(models.Model):
    name= models.CharField(max_length=50)


    def __str__(self):
        return self.name



class Coffe(models.Model):
    name = models.CharField(max_length= 50)
    been = models.ForeignKey(Been)
    roat = models.ForeignKey(Roast)
    esspresso = models.PositiveIntegerField(default=1)
    water = models.FloatField(default=0)
    steamed_milk = models.BooleanField(default=False)
    foam = models.FloatField
    poweder = models.ForeignKey(Powder)
    syrup = models.ForeignKey(Syrup)
    extra = models.TextField()
    myuser = models.ForeignKey(User)



    def __str__(self):
        return self.name

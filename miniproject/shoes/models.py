from django.db import models

# Create your models here.
class Brand(models.Model):
    def __str__(self):
        return self.name


class shoes(models.Model):
    S_id= models.CharField(max_length=10, unique=True)
    Brand = models.ForeignKey(Brand,null=True, blank=True,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100,)
    descrip = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    
    def __str__( self):
        return self.name    
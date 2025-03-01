from django.db import models


# Create your models here.
class Product:
    def __init__(self,brand,proid,images,proname,detail,price):
        self.brand = brand
        self.proid = proid
        self.images = images
        self.proname = proname
        self.detail = detail
        self.price = price

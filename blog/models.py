from unicodedata import name
from django.db import models


class Post(models.Model):
    tittle = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.tittle

class user(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField( "person's first name",max_length=50)
    datecreation = models.DateTimeField(auto_now=False, auto_now_add=True)
    number = models.BigIntegerField()
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField(max_length=254,default="")
    
    def __str__(self):
        return self.name

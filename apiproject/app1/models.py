from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=100,null=True)
    age=models.IntegerField(null=True)
    city=models.CharField(max_length=100,null=True)
    images=models.ImageField(null=True,blank=True,upload_to='media')
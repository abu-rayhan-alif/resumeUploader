from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=255)
    gender=models.CharField(max_length=20)
    pimage=models.ImageField(upload_to='pimages',blank=True)
    rdoc=models.FileField(upload_to='rdoc',blank=True)

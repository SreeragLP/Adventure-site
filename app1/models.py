from django.db import models

# Create your models here.

class AdventurePackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    image = models.ImageField(upload_to='adventure_package_images/')
    image1 = models.ImageField(upload_to='adventure_package_images/')
    image2 = models.ImageField(upload_to='adventure_package_images/')


    def __str__(self):
        return self.name


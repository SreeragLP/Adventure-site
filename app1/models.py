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


# models.py



class Rating(models.Model):
    RATING_CHOICES = (
        (1, 'Very Poor'),
        (2, 'Poor'),
        (3, 'Fair'),
        (4, 'Good'),
        (5, 'Excellent'),
    )

    rating = models.IntegerField(choices=RATING_CHOICES)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Rating: {self.rating}'

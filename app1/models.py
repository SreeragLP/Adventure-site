from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class AdventurePackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='adventure_package_images/')
    image1 = models.ImageField(upload_to='adventure_package_images/')
    location = models.CharField(max_length=100, null=True, blank=True)

    accommodation_price_per_person = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                                         blank=True)  # Add this line

    def __str__(self):
        return self.name

    def subtotal(self):
        return self.price


# models.py



# class Rating(models.Model):
#     RATING_CHOICES = (
#         (1, 'Very Poor'),
#         (2, 'Poor'),
#         (3, 'Good'),
#         (4, 'Very Good'),
#         (5, 'Excellent'),
#     )
#
#     rating = models.IntegerField(choices=RATING_CHOICES)
#     feedback = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'Rating: {self.rating}'




class Rating(models.Model):
    RATING_CHOICES = (
        (1, 'Very Poor'),
        (2, 'Poor'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(AdventurePackage, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    has_rated = models.BooleanField(default=False)

    def __str__(self):
        return f'Rating: {self.rating}'




class YourResponse(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject

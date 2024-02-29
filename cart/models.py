from django.db import models
from app1.models import AdventurePackage

from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    items=models.ForeignKey(AdventurePackage,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total_persons=models.IntegerField()
    date_added=models.DateField(auto_now_add=True)

    def subtotal(self):
        return self.total_persons*self.items.price
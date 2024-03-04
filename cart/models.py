from django.db import models
from app1.models import AdventurePackage
from django.contrib.auth.models import User


class Cart(models.Model):
    items = models.ForeignKey(AdventurePackage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_persons = models.IntegerField()
    selected_date = models.DateField()  # Add this field for selected date


    def subtotal(self):
        return self.total_persons*self.items.price




class Order(models.Model):
    package = models.ForeignKey(AdventurePackage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_persons = models.IntegerField()
    address = models.TextField(max_length=200)
    phone = models.CharField(max_length=200)
    order_status = models.CharField(max_length=30, default="pending")
    is_completed = models.BooleanField(default=False)
    selected_date = models.DateField()

    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

    def subtotal(self):
        return self.no_of_persons * self.package.price


class Account(models.Model):
    accnumber=models.IntegerField()
    acctype=models.CharField(max_length=200)
    balance=models.IntegerField()


    def __str__(self):
        return str (self.accnumber)
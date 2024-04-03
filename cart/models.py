from django.db import models
from app1.models import AdventurePackage
from django.contrib.auth.models import User


class Cart(models.Model):
    items = models.ForeignKey(AdventurePackage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_persons = models.IntegerField()
    selected_date = models.DateField()  # Add this field for selected date
    include_food_and_accommodation = models.BooleanField(default=False)
    accommodation_amount_per_person = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    # def subtotal(self):
    #     return self.total_persons*self.items.price

    # def subtotal(self):
    #     subtotal = self.total_persons * self.items.price
    #     if self.include_food_and_accommodation:
    #         subtotal += self.items.food_and_accommodation_price_per_person * self.total_persons
    #     return subtotal

    # def subtotal(self):
    #     subtotal = self.total_persons * self.items.price
    #     if self.include_food_and_accommodation and self.accommodation_amount_per_person:
    #         subtotal += self.accommodation_amount_per_person * self.total_persons
    #     return subtotal


    def subtotal(self):
        subtotal = self.total_persons * self.items.price
        if self.include_food_and_accommodation and self.accommodation_amount_per_person is not None:
            subtotal += self.total_persons * self.accommodation_amount_per_person
        return subtotal


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

    # def subtotal(self):
    #     return self.no_of_persons * self.package.price

    # def subtotal(self):
    #     subtotal = self.no_of_persons * self.package.price
    #     if self.package.food_and_accommodation_price_per_person:
    #         subtotal += self.no_of_persons * self.package.food_and_accommodation_price_per_person
    #     return subtotal

    def accommodation_subtotal(self):
        if self.package.accommodation_price_per_person:
            return self.no_of_persons * self.package.accommodation_price_per_person
        else:
            return 0

    def subtotal(self):
        return self.no_of_persons * self.package.price

    def total(self):
        return self.subtotal() + self.accommodation_subtotal()


class Account(models.Model):
    accnumber=models.IntegerField()
    acctype=models.CharField(max_length=200)
    balance=models.IntegerField()


    def __str__(self):
        return str (self.accnumber)
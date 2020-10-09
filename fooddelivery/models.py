from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    address = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)


def __str__(self):
    return f"{self.first_name}: {self.last_name}\t{self.email}\t{self.address}\t{self.contact}"


class Menu(models.Model):
    menu_version = models.CharField(max_length=200)
    other_details = models.CharField(max_length=200)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return f"{self.menu_version}: {self.other_details}\t{self.date_of_creation}\t{self.image_url}"


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=150)
    item_description = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=50, decimal_places=5)
    other_details = models.CharField(max_length=150)
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return f"{self.menu}: {self.item_name}\t{self.item_description}\t{self.item_price}\t{self.other_details}\t{self.image_url}"


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    restaurant_address = models.CharField(max_length=150)
    restaurant_contact = models.CharField(max_length=150)
    food_description = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.email}\t{self.owner}\t{self.restaurant_address}\t{self.restaurant_contact}"


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    staff_address = models.CharField(max_length=200)
    staff_contact = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user}: {self.staff_address}\t{self.staff_contact}"


class Meal(models.Model):
    menuitem = models.ForeignKey(MenuItem, on_delete=models.RESTRICT)
    customers = models.ManyToManyField(Customer, blank=True)
    status = models.CharField(max_length=200, default=False)
    address = models.CharField(max_length=200, default=False)
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=50, decimal_places=5)
    order_date = models.CharField(max_length=6)
    order_time = models.CharField(max_length=6)

from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a name of pizza")

    def __str__(self):
        return self.name

class Zakaz(models.Model):

    num_zakaz = models.CharField(max_length=10, help_text="Enter number of zakaz")
    pizza = models.ForeignKey('Pizza', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.num_zakaz

class Seller(models.Model):

    first_name = models.CharField(max_length=100, help_text="Enter a first_name of seller")
    last_name = models.CharField(max_length=100, help_text="Enter a last_name of seller")
    zakaz = models.ForeignKey('Zakaz', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Terminal(models.Model):
    zakaz = models.ForeignKey('Zakaz', on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey('Seller', on_delete=models.SET_NULL, null=True)
    time_open = models.DateField(null=True, blank=True)
    time_close = models.DateField(null=True, blank=True)
    total_pay = models.FloatField()

    def __str__(self):
        return f"номер заказа {self.zakaz} Итого: {self.total_pay}"


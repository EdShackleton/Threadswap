from django.db import models
from items.models import Item

# Create your models here.

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=10, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address_line_1 = models.CharField(max_length=40, blank=False)
    street_address_line_2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{0} @ {1}".format(self.item_name, self.original_price)
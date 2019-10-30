from django.db import models
from django.utils import timezone

class Item(models.Model):
    """ A single item """
    
    item_name = models.CharField(max_length=50)
    item_description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    size = models.IntegerField()
    original_price = models.IntegerField()
    image = models.ImageField(upload_to="img")
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title
    
    

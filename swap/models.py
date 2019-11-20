from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from items.models import Item

# Create your models here.

class SwapRequest(models.Model):
    """ A single item """
    requested_item_name = models.ForeignKey(Item.item_name, related_name="items", on_delete=models.CASCADE)
    requested_item_description = models.ForeignKey(Item.item_description, related_name="items", on_delete=models.CASCADE)
    requested_brand = models.ForeignKey(Item.brand, related_name="items", on_delete=models.CASCADE)
    requested_size = models.ForeignKey(Item.owner, related_name="items", on_delete=models.CASCADE)
    requested_original_price = models.ForeignKey(Item.original_price, related_name="items", on_delete=models.CASCADE)
    requested_image = models.ForeignKey(Item.image, related_name="items", on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True, on_delete=models.CASCADE)
    owner_of_item = models.ForeignKey(Item.owner, related_name="items", on_delete=models.CASCADE)
    requester = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    contact_number = models.IntegerField()
    top_size = models.IntegerField()
    waist_size = models.IntegerField()
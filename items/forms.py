from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('item_name', 'item_description', 'brand', 'size', 'original_price', 'image')
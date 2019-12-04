from django.shortcuts import render
from items.models import Item

# Create your views here.

def do_search_by_textbox(request):
    """To search for an item by textbox"""
    user_items = Item.objects.filter(item_name__icontains=request.GET['q'])
    return render(request, "items.html", {"items" : items})
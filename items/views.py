from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Item
from .forms import NewItemForm

def get_items(request):
    """Create a view that will return a list of all items and render them
    to the 'items.html' template"""
    
    items = Item.objects.filter(date_added__lte=timezone.now
        ()).order_by('-date_added')
    return render(request, "items.html", {"items" : items})

def item_detail(request, pk):
    """ Creates a view that shows a specific item based on the item ID (pk)
    and render it to the 'itemdetail.html' template, 
    or return a 404 error if not found"""
    
    item = get_object_or_404(Item, pk=pk)
    return render(request, "itemdetail.html", {"item" : item})

def create_or_edit_item(request, pk=None):
    """ Creates a view that allows us to create or edit an item
    if the post ID is null or not"""
    
    item = get_object_or_404(Item, pk=pk) if pk else None
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect(item_detail, item.pk)
    else:
        form = NewItemForm(instance=item)
    return render(request, 'newitemform.html', {'form' : form})
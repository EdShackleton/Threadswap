from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Item
from .forms import NewItemForm
from django.contrib.auth.decorators import login_required
from cart.contexts import cart_contents


def get_items(request):
    """Create a view that will return a list of all items and render them
    to the 'items.html' template"""
    user = request.user
    if request.user.is_authenticated():
        items = Item.objects.exclude(owner=user).filter(date_added__lte=timezone.now
            ()).order_by('-date_added')
    else:
        items = Item.objects.filter(date_added__lte=timezone.now
            ()).order_by('-date_added')
    return render(request, "items.html", {"items" : items, "profile": user})

def item_detail(request, pk):
    """ Creates a view that shows a specific item based on the item ID (pk)
    and render it to the 'itemdetail.html' template, 
    or return a 404 error if not found"""
    item = get_object_or_404(Item, pk=pk)
    return render(request, "itemdetail.html", {"item" : item})
    
def owner_item_detail(request, pk):
    """ Same as item_detail, but allow the owner to edit """
    item = get_object_or_404(Item, pk=pk)
    return render(request, "owneritemdetail.html", {"item" : item})

def edit_item(request, pk=None):
    """Create a view that allows us to create
    or edit an item depending if the Item ID
    is null or not"""
    item = get_object_or_404(Item, pk=pk) if pk else None
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect(item_detail, item.pk)
    else:
        form = NewItemForm(instance=item)
    return render(request, 'newitemform.html', {'form': form})

def create_item(request):
    """Create a view that allows us to create
    or edit an item depending if the Item ID
    is null or not"""
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        owner = request.user
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = owner
            item.save()
            return redirect(get_items)
    else:
        form = NewItemForm()
    return render(request, 'newitemform.html', {'form' : form})
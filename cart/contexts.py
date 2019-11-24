from django.shortcuts import get_object_or_404
from items.models import Item

def cart_contents(request):
    """
    Allows cart contents to be displayed on every page
    """
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    item_count = 0
    for id in cart.items():
        item = get_object_or_404(Item, pk=id)
        total += item.price
        cart_items.append({'id':id, 'item':item})
    
    return { 'cart_items':cart_items, 'total':total, 'item_count':item_count }
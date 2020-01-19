from django.shortcuts import render, redirect, reverse, get_object_or_404
from items.models import Item

# Create your views here.

def view_cart(request):
    """
    A view to render cart contents
    """
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    """
    A view to add item to cart
    """
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id])
        print("already in list - this will not add another")
    else:
        cart[id] = cart.get(id)
        print("not Found")
    
    request.session['cart'] = cart
    
    return redirect(reverse('view_cart'))

def delete_from_cart(request, id):
    """
    Delete an item from your cart
    """
    item = get_object_or_404(Item, id=id)
    print(id)
    print(item.id)
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
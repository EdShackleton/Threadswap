from django.shortcuts import render, redirect, reverse

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
    cart[id] = cart.get(id)
    
    request.session['cart'] = cart
    return redirect(reverse('get_items'))
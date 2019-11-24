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
    quantity = int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))
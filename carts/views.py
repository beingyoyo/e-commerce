from django.shortcuts import render, redirect
from carts.models import Cart, CartItem
from store.models import Product

# Create your views here.
def cart(request):
    return render(request, 'store/cart.html')

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()

def add_cart(request, product):
    product = Product.objects.get(id = product_id) #Get the product
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request)) #Get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1 #increase cart items value
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,

        )
        cart_item.save()
    return redirect('cart')
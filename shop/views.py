from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart')

def view_cart(request):
    items = CartItem.objects.all()
    total = sum(item.total_price() for item in items)
    return render(request, 'cart.html', {'items': items, 'total': total})

def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.quantity += 1
    item.save()
    return redirect('cart')

def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart')

def remove_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart')

def checkout(request):
    CartItem.objects.all().delete()
    return render(request, 'success.html')
from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from product.models import Product
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm
from coupons.forms import CouponActivatedForm


def cart_detail(request):
    """shopping cart detail"""

    cart = Cart(request)
    update_quantity_form = CartAddProductForm(request.POST)
    coupons_activated_form = CouponActivatedForm()
    return render(request, 'cart_detail.html', {'cart': cart,
                                                'coupons_activated_form': coupons_activated_form,
                                                'update_quantity_form': update_quantity_form,
                                                })


@require_POST
def cart_add(request, product_id):
    """adding the product to the cart"""

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    """removing the product from the cart"""

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

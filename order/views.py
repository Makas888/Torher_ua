from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from Torcher_ua.settings import DEFAULT_FROM_EMAIL
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    """
    Creating an order, and if the order is successfully created, sending an email to the user's email
    """
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            request.session['coupon_id'] = None
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            subject = f'Замовлення № {order.pk}'
            message = f"Вітаю {order.first_name} {order.last_name}! Ваше замовлення №{order.pk}, " \
                      f"на суму {order.get_total_cost()}грн створене, " \
                      f"наш менеджер зв'яжеться з вами для уточнення умов оплати та передачі замовлення"
            try:
                send_mail(subject, message, DEFAULT_FROM_EMAIL, [order.email])
                messages.success(request, 'Лист з номером замовлення відправлено на ваш EMAIL.')
            except:
                messages.error(request, 'Повідомлення не надіслано на ваш EMAIL.')
            messages.success(request, f"Замовлення №:'{order.pk}' створене, "
                                      f"наш менеджер у найближчий час з вами зв'яжеться")
            cart.clear()
            return redirect('product:products_list')
        else:
            messages.error(request, 'Упс, щось пішло не так:)!\n Перевірте коректність введенної шнформації.')
            return render(request, 'order_create.html', {'cart': cart, 'form': form})
    else:
        form = OrderCreateForm
    return render(request, 'order_create.html', {'cart': cart, 'form': form})

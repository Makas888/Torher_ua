from django.shortcuts import render, redirect
from contacts_page.models import UserMessage
from order.models import Order
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    """checking whether the user belongs to the 'manager' group"""

    return user.groups.filter(name='Менеджер').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def message_list(request):
    """list of messages from customers, just not read"""

    messages = UserMessage.objects.filter(archived=False)
    return render(request, 'messages.html', context={'message_list': messages})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def add_archive(request, pk):
    """mark a message from the client as read"""

    UserMessage.objects.filter(pk=pk).update(archived=True)
    return redirect('manager:message_list')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def orders_list(request):
    """list of unprocessed orders"""

    orders = Order.objects.filter(processed=False)
    return render(request, 'orders.html', context={'orders_list': orders})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def processed(request, pk):
    """mark processed order"""

    Order.objects.filter(pk=pk).update(processed=True)
    return redirect('manager:orders_list')

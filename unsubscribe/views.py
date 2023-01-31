from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from news_letter_form.models import Newsletter


def news_latter_unsubscribe(request, email_pk):
    """display with a button confirm to unsubscribe from the newsletter"""

    if request.method == 'POST':
        try:
            email = get_object_or_404(Newsletter, pk=email_pk)
            email.delete()
            messages.success(request, 'Вітаю, ви відписались від новин!')
        except:
            messages.error(request, f'Ви вже відписані від розсилки, якщо листи ще досі приходять, '
                                    f'напишіть нам у розділі "контакти"')
            return render(request, 'unsubscribe.html')

        return redirect('/')
    return render(request, 'unsubscribe.html', )

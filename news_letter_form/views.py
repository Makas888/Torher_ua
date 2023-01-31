from django.shortcuts import redirect
from news_letter_form.forms import NewsLetterForm
from django.contrib import messages


def news_letter_view(request):
    form = NewsLetterForm(request.POST or None)
    if form.is_valid():
        try:
            form.save()
            messages.success(request, 'Ви підписані на розсилку.')
            return redirect('/')
        except:
            messages.info(request, 'Ви підписались раніше.')
    else:
        messages.info(request, 'Ви підписались раніше.')
        return redirect('/')

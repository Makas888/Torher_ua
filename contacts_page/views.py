from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactList
from .forms import UserMessageForm


def contacts_page_view(request):
    """display of contact information, feedback form"""

    contacts = get_object_or_404(ContactList, is_visible=True)

    form_massage = UserMessageForm(request.POST or None)
    if request.method == 'POST':
        if form_massage.is_valid():
            form_massage.save()
            messages.success(request, 'Ваше повідомлення успішно відправлено, '
                                      'наш менеджер відповість вам у найближчий час.')
            return redirect('/')
        else:
            messages.error(request, 'Упс, щось пішло не так:)!\n Перевірте коректність введенної шнформації.')
    return render(request, 'contacts_view.html', {'contacts': contacts,
                                                  'form_massage': form_massage,
                                                  })

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import ContactForm
from Torcher_ua.settings import DEFAULT_FROM_EMAIL
from news_letter_form.models import Newsletter


def contact_view(request):
    """displaying the form for starting the mailing"""

    email_list = Newsletter.objects.all()
    email_list = [item for item in email_list.all()]
    # якщо метод GET, повернемо форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # якщо метод POST, повернемо форму и відправимo листи
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                for email in email_list:
                    link_unsubscribe = render_to_string('link_unsubscribe.html', {
                        'email_pk': email.pk,
                        'domain': get_current_site(request).domain,
                        'protocol': 'https' if request.is_secure() else 'http'
                    })
                    message1 = message + '\n' + link_unsubscribe
                    msg = EmailMultiAlternatives(subject, message1, DEFAULT_FROM_EMAIL, [email.email])
                    msg.attach_alternative(message1, "text/html")
                    msg.send()
            except BadHeaderError:
                messages.error(request, 'Помилка у темі листа.')
            messages.success(request, 'Листи з новинами відправлено підписникам.')
            return render(request, "email.html", {'form': form})
    else:
        messages.error(request, 'Неправильний запит.')
        return HttpResponse('Неправильний запит.')
    return render(request, "email.html", {'form': form})

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from .forms import UserRegistrationForm, UserLogin, PasswordRecoveryForm, PasswordResForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.db.models.query_utils import Q


def activate(request, uidb64, token):
    """activation of the user account after clicking on the link from the email"""

    user = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Дякуємо за підтвердження електронної адреси, тепер ви можете '
                                  'активувати свій профіль на нашому сайті.')
        return redirect('login')
    else:
        messages.error(request, 'Посилання активації не є дійсне, спроьуйте ще раз.')
    return redirect('/')


def activate_email(request, user, to_email):
    """
    sending an email with a confirmation link that is valid for 4 hours
    to a user who registers in the system
    """

    mail_subject = 'Активуйте свій аккаунт'
    message = render_to_string('template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMultiAlternatives(mail_subject, message, to=[to_email])
    email.attach_alternative(message, "text/html")
    if email.send():
        messages.success(request, f'Шановний <b>{user}</b>, перейдіть до вашої поштової скриньки <b>{to_email}</b> '
                                  f'і натисніть отримане посилання активації, щоб підтвердити та завершити реєстрацію.'
                                  f'<b>Примітка:</b> Перевірте репозиторій спаму.')
    else:
        user.delete()
        messages.error(request, f'Не вдалося надіслати електронний лист на адресу {to_email}. '
                                f'Перевірте, чи правильно ви його ввели')


def login_view(request):
    """user activation in the system, login and password"""

    login_form = UserLogin(request.POST or None)
    next_get = request.GET.get('next')

    if request.method == 'POST':

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Вітаю {user.username}!, ви авторизовані, приємних покупок!')

            next_post = request.POST.get('next')

            return redirect(next_get or next_post or '/')
        else:
            for error in list(login_form.errors.values()):
                messages.error(request, error)

    return render(request, 'login.html', context={'login_form': login_form})


def registration_view(request):
    """
    two forms:
    1. creating a user and sending an email to activate the profile.
    2. user activation in the system
    """

    user_registration_form = UserRegistrationForm(request.POST or None)
    login_form = UserLogin(request.POST or None)

    if user_registration_form.is_valid():
        new_user = user_registration_form.save(commit=False)
        new_user.is_active = False
        new_user.set_password(user_registration_form.cleaned_data['password1'])
        new_user.save()
        activate_email(request, new_user, user_registration_form.cleaned_data.get('email'))

        return redirect('/')

    elif login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        login(request, user)

        next_post = request.POST.get('next')
        return redirect(next_post or '/')
    else:
        for error in list(user_registration_form.errors.values()):
            messages.error(request, error)
        for error in list(login_form.errors.values()):
            messages.error(request, error)

    return render(request, 'registration.html', context={'user_registration_form': user_registration_form,
                                                         'login_form': login_form})


def logout_view(request):
    """logout user"""

    logout(request)
    return redirect('/')


def password_recovery_view(request):
    """password change form, if the user is activated in the system"""

    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = PasswordRecoveryForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Ваш пароль змінено')
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
        form = PasswordRecoveryForm(user)
        return render(request, 'password_recovery.html', {'form': form})
    else:
        return redirect('login')


def password_reset_view(request):
    """
    if the user forgot the password, he must enter the email that was used during registration,
    sending a letter with a token valid for 4 hours, with a request to reset the password
    """

    if request.method == 'POST':
        form = PasswordResForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = 'Запит скидання паролю'
                message = render_to_string('template_reset_password.html', {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    'protocol': 'https' if request.is_secure() else 'http'
                })
                email = EmailMultiAlternatives(subject, message, to=[associated_user.email])
                email.attach_alternative(message, "text/html")
                if email.send():
                    messages.success(request, f'<h2>Скидання пароля надіслано</h2><hr> '
                                              f'<p> Ми надіслали вам електронною поштою інструкції щодо встановлення '
                                              f'пароля,якщо існує обліковий запис із вказаною вами електронною поштою. '
                                              f'Ви повинні отримати їх найближчим часом.'
                                              f'<br>Якщо ви не отримаєте електронний лист, будь ласка, переконайтеся, '
                                              f'що ви ввели адресу, яку ви зареєстрували, і перевірте папку зі спамом.'
                                              f'</p>')
                else:
                    messages.error(request, 'Не вдалося надіслати електронний лист для скидання пароля,'
                                            ' <b>SERVER PROBLEM</b>')

            return redirect('/')

    form = PasswordResForm()
    return render(request, 'password_reset.html', {'form': form})


def password_reset_confirm(request, uidb64, token):
    """
    after clicking on the link in the letter,
    the user confirms the reset of the password and enters a new one, the password is saved
    """

    user = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = PasswordRecoveryForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Ваш пароль встановлено. Ви можете <b>увійти </b> зараз.")
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = PasswordRecoveryForm(user)
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Термін дії посилання закінчився")

    messages.error(request, 'Щось пішло не так, переспрямування назад на домашню сторінку')
    return redirect("/")

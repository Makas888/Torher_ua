from django import forms
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm, UserChangeForm, UserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate, get_user_model
from captcha.fields import CaptchaField


class UserLogin(forms.Form):
    """user authorization"""

    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'type': "text"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'type': "password"}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError('Пароль або логін вказані не вірно')

        return super().clean()


class UserRegistrationForm(UserCreationForm):
    """user registration"""

    password1 = forms.CharField(label='Пароль*', widget=forms.PasswordInput(attrs={"placeholder": "пароль*",
                                                                                   "type": "password",
                                                                                   "tabindex": "4"}))
    password2 = forms.CharField(label='Повтор паролю*',
                                widget=forms.PasswordInput(attrs={"placeholder": "повтор паролю*",
                                                                  "type": "password",
                                                                  "tabindex": "4"})
                                )

    class Meta:
        model = CustomUser
        fields = ('username', 'last_name', 'email', 'phone', 'gender', 'groups')
        widgets = {'username': forms.TextInput(attrs={'placeholder': "Ім'я*",
                                                      'type': "text",
                                                      'tabindex': "1"}),
                   'last_name': forms.TextInput(attrs={'placeholder': "Прізвище",
                                                       'type': "text",
                                                       'tabindex': "1"}),
                   'email': forms.EmailInput(attrs={'placeholder': "email*",
                                                    'type': "email",
                                                    'tabindex': "3"}),
                   'phone': forms.TextInput(attrs={'placeholder': "Телефон",
                                                   'type': "text",
                                                   'tabindex': "3"}),
                   'gender': forms.RadioSelect(),
                   }

    def clean_password2(self):
        data = self.cleaned_data

        if data['password1'] == data['password2']:
            return data['password2']

        raise forms.ValidationError('Паролі не співпадають')


class PasswordRecoveryForm(SetPasswordForm):
    """password change"""

    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']


class PasswordResForm(PasswordResetForm):
    """password reset captcha"""

    captcha = CaptchaField()


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'last_name', 'email', 'phone', 'gender')

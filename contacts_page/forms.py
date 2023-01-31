from django import forms
from .models import UserMessage
from captcha.fields import CaptchaField


class UserMessageForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = UserMessage
        fields = {'name': forms.CharField, 'email': forms.EmailField, 'phone': forms.CharField,
                  'message': forms.CharField}
        widgets = {'name': forms.TextInput(attrs={'type': "text",
                                                  'class': "textbox",
                                                  }),
                   'email': forms.EmailInput(attrs={'type': "email",
                                                    'class': "textbox",
                                                    }),
                   'phone': forms.TextInput(attrs={'type': "text",
                                                   'class': "textbox",
                                                   }),
                   'message': forms.Textarea({'type': "text",
                                              'class': "textbox",
                                              }),
                   }

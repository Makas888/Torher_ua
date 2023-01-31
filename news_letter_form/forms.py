from django import forms

from .models import Newsletter


class NewsLetterForm(forms.ModelForm):
    """form for entering e-mail for subscribing to the newsletter"""

    class Meta:
        model = Newsletter
        fields = ('email', )
        widgets = {'email': forms.EmailInput(attrs={'type': 'email',
                                                    'class': 'email',
                                                    'value': 'Ваш Email',
                                                    'onfocus': "this.value = '';",
                                                    'onblur': "if (this.value == '') {this.value = 'Ваш Email';}",
                                                    })
                   }
        labels = {
                  'email': ''
                 }

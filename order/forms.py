from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """a form for filling in the data necessary to create an order"""

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'department_number', 'city', 'message']
        widgets = {'first_name': forms.TextInput(attrs={'type': "text",
                                                        'class': "textbox"}),
                   'last_name': forms.TextInput(attrs={'type': "text",
                                                       'class': "textbox"}),
                   'email': forms.EmailInput(attrs={'type': "email",
                                                    'class': "textbox"}),
                   'phone': forms.TextInput(attrs={'type': 'text',
                                                   'class': "textbox"}),
                   'address': forms.TextInput(attrs={'type': "text",
                                                     'class': "textbox"}),
                   'department_number': forms.TextInput(attrs={'type': "text",
                                                               'class': "textbox"}),
                   'message': forms.Textarea(attrs={'type': "text",
                                                    'class': "textbox"}),
                   }

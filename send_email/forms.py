from django import forms


class ContactForm(forms.Form):
    """
    a form for starting a mailing to subscribers
    with the subject and body of the letter
    """

    subject = forms.CharField(label='Тема', required=True)
    message = forms.CharField(label='Повідомлення', widget=forms.Textarea)

from django import forms


class CartAddProductForm(forms.Form):
    """a form for adding a product to the cart or updating the quantity"""

    quantity = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'item_quantity',
                                                                                     'type': 'number',
                                                                                     'value': '1',
                                                                            }))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

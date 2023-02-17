from django import forms


class CartAddProductForm(forms.Form):
    """a form for adding a product to the cart or updating the quantity"""

    quantity = forms.IntegerField(label='',
                                  min_value=1,
                                  max_value=999,
                                  widget=forms.NumberInput(attrs={'class': 'item_quantity',
                                                                  'type': 'number',
                                                                  'value': '1',
                                                                  }))
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

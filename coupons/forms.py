from django import forms


class CouponActivatedForm(forms.Form):
    code = forms.CharField(label='Купон на знижку')

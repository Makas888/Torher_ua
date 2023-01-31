import django_filters
from django import forms
from product.models import Product


class ProductFiltering(django_filters.FilterSet):
    discount = django_filters.AllValuesMultipleFilter(widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
                                                      label='Знижка',
                                                      field_name='discount')
    price = django_filters.RangeFilter()
    type_product = django_filters.AllValuesMultipleFilter(widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
                                                          label='Тип товару',
                                                          field_name='type_product__name',)
    brand = django_filters.AllValuesMultipleFilter(widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
                                                   label='Бренд',
                                                   field_name='brand__name',)

    class Meta:
        model = Product
        fields = ['discount', 'price', 'type_product', 'brand']

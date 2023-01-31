from django import template
from product.models import Category, SubCategory, Brands

register = template.Library()


@register.inclusion_tag('header/tags/header.html')
def header_view():
    brands = Brands.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    return {'brands': brands,
            'categories': categories,
            'subcategories': subcategories,
            }

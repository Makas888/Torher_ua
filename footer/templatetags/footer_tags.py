from django import template
from product.models import Category

register = template.Library()


@register.inclusion_tag('footer/tags/footer.html')
def footer_view():
    categories = Category.objects.all()
    return {'categories': categories}


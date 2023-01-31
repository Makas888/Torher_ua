from django import template
from news_letter_form.forms import NewsLetterForm

register = template.Library()


@register.inclusion_tag('contact/tags/news_letter_form.html')
def news_letter_form():
    return {'news_letter_form': NewsLetterForm()}

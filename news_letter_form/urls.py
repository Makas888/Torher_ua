from django.urls import path
from .views import news_letter_view

app_name = 'news_letter_form'

urlpatterns = [
    path('', news_letter_view, name='news_letter')
]

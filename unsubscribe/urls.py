from django.urls import path
from .views import news_latter_unsubscribe

app_name = 'unsubscribe'

urlpatterns = [
    path('', news_latter_unsubscribe, name='unsubscribe'),

]

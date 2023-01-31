from django.urls import path
from .views import order_create

app_name = 'order'

urlpatterns = [
    path('', order_create, name='order'),
]

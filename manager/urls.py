from django.urls import path
from .views import message_list, add_archive, orders_list, processed

app_name = 'manager'

urlpatterns = [
    path('messages/', message_list, name='message_list'),
    path('update/<int:pk>/', add_archive, name='add_archive'),
    path('orders/', orders_list, name='orders_list'),
    path('processed/<int:pk>/', processed, name='processed'),

    ]

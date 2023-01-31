from django.urls import path
from .views import products_list, product_detail

app_name = 'product'

urlpatterns = [
    path('', products_list, name='products_list'),
    path('<slug:slug>/', products_list, name='product_list_by_category'),
    path('<int:id_>/<slug:slug>/', product_detail, name='product_detail'),
]

from django.urls import path
from .views import coupon_activated

app_name = 'coupons'

urlpatterns = [
    path('activated/', coupon_activated, name='activated_coupon'),

]

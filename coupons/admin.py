from django.contrib import admin
from .models import SubjectCoupons, Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['subject', 'code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['subject', 'valid_from', 'valid_to', 'active']
    search_fields = ['code']


admin.site.register(SubjectCoupons)

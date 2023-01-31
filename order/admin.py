from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """product search from a specific order in the admin panel"""

    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    """displaying the orders in the admin panel"""

    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'department_number',
                    'city', 'processed', 'created', 'updated', 'message']
    list_display_links = ['id', 'first_name', 'last_name', 'email', 'address', 'message']
    list_filter = ['processed', 'created', 'updated']
    inlines = [OrderItemInline]
    list_editable = ['processed']


admin.site.register(Order, OrderAdmin)

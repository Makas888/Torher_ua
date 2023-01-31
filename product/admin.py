from django.contrib import admin
from product.models import SubCategory, Brands, Discount, Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price', 'type_product', 'stock', 'discount', 'article', 'is_active']
    list_filter = ['is_active', 'type_product', 'brand', 'discount']
    list_editable = ['price', 'stock',  'article', 'discount', 'is_active']

    prepopulated_fields = {'slug': ('title', )}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name', ]

    prepopulated_fields = {'slug': ('name', )}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name', ]

    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Brands)
admin.site.register(Discount)

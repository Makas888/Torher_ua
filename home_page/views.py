from django.shortcuts import render
from product.models import Brands, Product, Category, SubCategory
from .models import HeroSection, SeasonSaleVisible
import random


def home_page_view(request):
    """displaying the start page"""

    brands = Brands.objects.all()
    categories = Category.objects.all()
    slides = HeroSection.objects.filter(is_visible=True)
    subcategories = SubCategory.objects.all()
    products = Product.objects.exclude(discount__percent=0)
    products = random.sample(list(products), len(products[:8]))
    sales = SeasonSaleVisible.objects.get(is_visible=True)
    return render(request, 'base.html', {'brands': brands,
                                         'categories': categories,
                                         'slides': slides,
                                         'subcategories': subcategories,
                                         'products': products,
                                         'sales': sales,
                                         })

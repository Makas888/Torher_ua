from django.core.paginator import Paginator

from .filters import ProductFiltering
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Product, Category, Brands, SubCategory, Discount


def products_list(request, slug=None):
    """display of goods depending on the applied filters"""

    product_filter = ProductFiltering(request.GET, queryset=Product.objects.filter(is_active=True))

    cart_product_form = CartAddProductForm()
    discount_product = Discount.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    brands = Brands.objects.all()
    if slug and SubCategory.objects.filter(slug=slug):
        type_products = get_object_or_404(SubCategory, slug=slug)
        product_filter = ProductFiltering(queryset=Product.objects.filter(is_active=True, type_product=type_products))
    if slug and Category.objects.filter(slug=slug):
        category = get_object_or_404(Category, slug=slug)
        product_filter = ProductFiltering(queryset=Product.objects.filter(type_product__in=category.parent.all()))

    paginator = Paginator(product_filter.qs, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if request.htmx:
        base_template = '_partial.html'
    else:
        base_template = 'product_filter.html'

    return render(request, 'list-product.html', {'categories': categories[:10],
                                                 'discount_product': discount_product,
                                                 'subcategories': subcategories,
                                                 'brands': brands,
                                                 'cart_product_form': cart_product_form,
                                                 'base_template': base_template,
                                                 'page_obj': page_obj,
                                                 })


def product_detail(request, id_, slug):
    """displaying the details of a certain product"""

    cart_product_form = CartAddProductForm()
    product = get_object_or_404(Product, id=id_, slug=slug, is_active=True)
    products = Product.objects.filter(type_product=product.type_product).order_by('title')

    paginator = Paginator(products, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if request.htmx:
        base_template = '_partial.html'
    else:
        base_template = 'product_detail.html'

    return render(request, 'list-product-from-category.html', {'product': product,
                                                               'page_obj': page_obj,
                                                               'cart_product_form': cart_product_form,
                                                               'base_template': base_template,
                                                               })


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
    return render(request, 'product_filter.html', {'categories': categories[:10],
                                                   'discount_product': discount_product,
                                                   'subcategories': subcategories,
                                                   'brands': brands,
                                                   'cart_product_form': cart_product_form,
                                                   'product_filter': product_filter.qs,
                                                   })


def product_detail(request, id_, slug):
    """displaying the details of a certain product"""

    cart_product_form = CartAddProductForm()
    product = get_object_or_404(Product, id=id_, slug=slug, is_active=True)
    products = Product.objects.filter(type_product=product.type_product)
    return render(request, 'product_detail.html', {'product': product,
                                                   'products': products,
                                                   'cart_product_form': cart_product_form,
                                                   })


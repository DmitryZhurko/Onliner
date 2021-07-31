from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from shop.forms import OrderForm
from shop.models import ProductCategory, Product, Basket, Order

def paginator(request, name):

    paginator = Paginator(name, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request, category_id=None, page=1):
    categories = ProductCategory.objects.all()
    baskets = Basket.objects.filter(user=request.user)
    total_quantity = 0
    for _ in baskets:
        total_quantity += 1

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    page_obj = paginator(request, products)

    context = {
        'categories': categories,
        'total_quantity': total_quantity,
        'baskets': baskets,
        'page_obj': page_obj
    }
    return render(request, 'shop/index.html', context)


def product_detail(request, product_id):
    categories = ProductCategory.objects.all()
    products = Product.objects.get(pk=product_id)
    baskets = Basket.objects.filter(user=request.user)
    total_quantity = 0
    for _ in baskets:
        total_quantity += 1
    context = {
        'product': products,
        'categories': categories,
        'baskets': baskets,
        'total_quantity': total_quantity,
    }
    return render(request, 'shop/product_detail.html', context)


def shopping_cart(request):
    categories = ProductCategory.objects.all()
    baskets = Basket.objects.filter(user=request.user)
    total_quantity = 0
    total_sum = 0
    for basket in baskets:
        total_quantity += 1
        total_sum += basket.sum()

    context = {
        'categories': categories,
        'baskets': baskets,
        'total_quantity': total_quantity,
        'total_sum': total_sum,
    }
    return render(request, 'shop/shopping_cart.html', context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_delete(request, product_id):
    product = Basket.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def checkout(request):
    categories = ProductCategory.objects.all()
    baskets = Basket.objects.filter(user=request.user)
    total_quantity = 0
    total_sum = 0
    for basket in baskets:
        total_quantity += 1
        total_sum += basket.sum()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            of = order_form.save(commit=False)

            order = Order.objects.create(
                user=request.user,
                total_price=total_sum,
                email=of.email,
                tel=of.tel,
                #как-то отправить продуты
            )
            order.save()

            return redirect('shop:user_orders')
    else:
        order_form = OrderForm()
    context = {
        'categories': categories,
        'baskets': baskets,
        'total_quantity': total_quantity,
        'total_sum': total_sum,
        'order_form': order_form,
    }
    return render(request, 'shop/checkout.html', context)


def user_orders(request):
    orders = Order.objects.filter(user=request.user)

    return render(request, 'shop/confirm_order.html', {'orders': orders})


# def confirm_order(request):
#     order = Order.objects.filter(user=request.user).first()
#     products = basket.product.all()
#     total_price = 0
#     for bas in basket:
#         total_price += bas.sum()
#     order = Order.objects.create(user=request.user, total_price=total_price)
#     order.products.add(*products)
#
#     basket.product.clear()
#     return redirect('user_orders')


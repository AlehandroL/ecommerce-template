from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .basket import Basket
from store.models import Product

def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket':basket})

def basket_add(request):
    basket = Basket(request)
    if request.POST.get("action") == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, product_qty=product_qty)
        basket_qty = basket.__len__()
        response = JsonResponse({'basket_qty':basket_qty})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        basket.delete(product=product)
        basket_qty = basket.__len__()
        subtotal = basket.get_total_price()
        response = JsonResponse({'basket_qty':basket_qty, 'subtotal':subtotal})
        return response

def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product, product_qty=product_qty)
        basket_qty = basket.__len__()
        subtotal = basket.get_total_price()
        response = JsonResponse({'basket_qty':basket_qty, 'subtotal':subtotal})
        return response

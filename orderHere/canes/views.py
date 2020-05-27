from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Order
from .forms import OrderForm


def delete_order(req, id):
    order = get_object_or_404(Order, id=id)
    if req.method == 'POST':
        order.delete()
        return redirect('canes:homepage')
    context = {
        "orders": Order.objects.all
    }
    return render(req, "main/delete.html", context)


def order_page(req):
    if req.method == 'POST':
        form = OrderForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('canes:thanks')
    form = OrderForm
    return render(req, "main/order.html", {"form": form})


def homepage(req):
    return render(req, 'main/index.html', context={'orders': Order.objects.all})


def complete(req):
    return render(req, "main/thanks.html")

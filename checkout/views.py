from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There is nothing in your bag at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Q3yahDMCIasDIh7ZVIwOdD4W99ZOgNi2aLWIau9RW9XieM11qw81stSrLehFx81GE5asmRBnCI62ZChFnuxf1ui00K02HGMUW',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
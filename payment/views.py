from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe

from .mixins import ItemCheckoutSessionMixin, OrderCheckoutSessionMixin
from .models import Item, OrderItem, Order


stripe.api_key = settings.STRIPE_PRIVATE_KEY


class ItemsListView(ListView):
    model = Item
    template_name = 'items_list.html'
    context_object_name = 'items'


class ItemView(TemplateView):
    template_name = 'item.html'

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        context['item'] = Item.objects.get(pk=kwargs['pk'])
        context['STRIPE_PUBLISHABLE_KEY'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


class BuyView(ItemCheckoutSessionMixin, View):

    def get(self, request, *args, **kwargs):
        session = self._generate_session(self, request, *args, **kwargs)
        return JsonResponse({'id': session.id})

    def post(self, request, *args, **kwargs):
        session = self._generate_session(self, request, *args, **kwargs)
        return redirect(session.url, code=303)

@login_required
def add_to_cart(request, **kwargs):
    item_pk = kwargs['pk']
    item = get_object_or_404(Item, pk=item_pk)
    # create or get an instance of OrderItem
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    # check if the user already has an unordered order
    if order_qs.exists():
        order = order_qs[0]
        # check if the item is already in order
        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect(reverse('retrieve_item', kwargs={'pk': item_pk}))
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect(reverse('retrieve_item', kwargs={'pk': item_pk}))
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect(reverse('retrieve_item', kwargs={'pk': item_pk}))


def remove_from_cart(request, **kwargs):
    item_pk = kwargs['pk']
    item = get_object_or_404(Item, pk=item_pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    # check if the user already has an unordered order
    if order_qs.exists():
        order = order_qs[0]
        # check if the item is already in order
        if order.items.filter(item__pk=item.pk).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect(reverse('cart'))


class OrderView(ListView):
    model = Order
    template_name = 'cart.html'
    context_object_name = 'order'
    redirect_field_name = ''

    def get_queryset(self):
        order_qs = Order.objects.filter(user=self.request.user, ordered=False)
        if order_qs.exists():
            return order_qs[0]
        return order_qs

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['STRIPE_PUBLISHABLE_KEY'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


class CheckoutView(OrderCheckoutSessionMixin, View):

    def get(self, request, *args, **kwargs):
        session = self._generate_session(self, request, *args, **kwargs)
        return JsonResponse({'id': session.id})

    def post(self, request, *args, **kwargs):
        session = self._generate_session(self, request, *args, **kwargs)
        return redirect(session.url, code=303)

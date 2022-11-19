from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse
from django.conf import settings
import stripe

from .mixins import CheckoutSessionMixin
from .models import Item


stripe.api_key = settings.STRIPE_PRIVATE_KEY


class ItemsListView(ListView):
    model = Item
    template_name = 'items_list.html'


class ItemView(TemplateView):
    template_name = 'item.html'

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        context['item'] = Item.objects.get(pk=kwargs['pk'])
        context['STRIPE_PUBLISHABLE_KEY'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


class BuyView(CheckoutSessionMixin, View):

    def get(self, request, *args, **kwargs):
        session = self._generate_session(self, request, *args, **kwargs)
        return JsonResponse({'id': session.id})

    def post(self, request, *args, **kwargs):
        session = self._generate_session(self, request, *args, **kwargs)
        return redirect(session.url, code=303)

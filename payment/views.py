from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
import stripe

from .models import Item
from config import settings


class ItemView(TemplateView):
    template_name = 'item.html'

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        context['item'] = Item.objects.get(pk=kwargs['pk'])
        context['STRIPE_PUBLISHABLE_KEY'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


stripe.api_key = settings.STRIPE_PRIVATE_KEY


class BuyView(View):

    def get(self, request, *args, **kwargs):
        item_id = kwargs['pk']
        item = Item.objects.get(id=item_id)
        checkout_session = stripe.checkout.Session.create(
                    line_items=[
                        {
                            'price_data': {
                                'currency': 'usd',
                                'unit_amount_decimal': item.get_price(),
                                'product_data': {
                                    'name': item.name,
                                    'description': item.description
                                },
                            },
                            'quantity': 1,
                        },
                    ],
                    mode='payment',
                    success_url=settings.RANDOM_TEST_URL,
                    cancel_url=settings.RANDOM_TEST_URL,
                )
        return JsonResponse({'id': checkout_session.id})
from django.conf import settings
import stripe

from payment.models import Item


class CheckoutSessionMixin:
    def _generate_session(self, request, *args, **kwargs):
        item_id = kwargs['pk']
        item = Item.objects.get(id=item_id)
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
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
        return session

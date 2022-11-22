from django.conf import settings
import stripe

from payment.models import Item, Order


class ItemCheckoutSessionMixin:

    def generate_session(self, request, *args, **kwargs):
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
            success_url=settings.DUMMY_URL,
            cancel_url=settings.DUMMY_URL,
        )
        return session


class OrderCheckoutSessionMixin:

    def generate_session(self, request, *args, **kwargs):
        order_id = kwargs['pk']
        order = Order.objects.get(id=order_id)
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': order.get_total(),
                        'product_data': {
                            'name': f'Your order ID: {order.id}',
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.DUMMY_URL,
            cancel_url=settings.DUMMY_URL,
        )
        return session

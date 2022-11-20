from django.urls import path

from payment.views import (ItemsListView,
                           ItemView, BuyView,
                           add_to_cart, remove_from_cart,
                           OrderView, CheckoutView)

urlpatterns = [
    path('', ItemsListView.as_view(), name='items_list'),
    path('item/<int:pk>/', ItemView.as_view(), name='retrieve_item'),
    path('buy/<int:pk>/', BuyView.as_view(), name='buy_item'),
    path('checkout/<int:pk>/', CheckoutView.as_view(), name='checkout'),
    path('cart/', OrderView.as_view(), name='cart'),
    path('add-to-cart/<int:pk>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:pk>',
         remove_from_cart,
         name='remove-from-cart')
]

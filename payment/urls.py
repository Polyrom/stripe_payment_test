from django.urls import path

from payment.views import ItemView, BuyView

urlpatterns = [
    path('item/<int:pk>/', ItemView.as_view(), name='retrieve_item'),
    path('buy/<int:pk>/', BuyView.as_view(), name='buy_item'),
]

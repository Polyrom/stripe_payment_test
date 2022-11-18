from django.urls import path

from payment.views import ItemsListView, ItemView, BuyView

urlpatterns = [
    path('', ItemsListView.as_view(), name='items_list'),
    path('item/<int:pk>/', ItemView.as_view(), name='retrieve_item'),
    path('buy/<int:pk>/', BuyView.as_view(), name='buy_item'),
]

from django.urls import path

from payment.views import ItemView, ItemsListView

urlpatterns = [
    path('items/', ItemsListView.as_view(), name='items_list'),
    path('item/<int:pk>/', ItemView.as_view(), name='item_view'),
]
from rest_framework.generics import ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item
from .serializers import ItemSerializer


class ItemsListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item.html'

    def get(self, request, *args, **kwargs):
        queryset = Item.objects.get(pk=kwargs['pk'])
        return Response({'item': queryset})

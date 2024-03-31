
from.serializers import ProductSerializer
from.models import product
from rest_framework  import viewsets

class ProducteViewSet(viewsets.ModelViewSet):
    queryset=product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    
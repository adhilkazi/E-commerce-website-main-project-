from rest_framework import serializers
from.models  import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Order
        fields=('__all__')
        #todo:ad product and quantity
        
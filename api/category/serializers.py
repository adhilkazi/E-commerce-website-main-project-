from  rest_framework import serializers
from .models import category

class categorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=category
        fields=('name','description')
 

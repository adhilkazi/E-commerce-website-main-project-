from django.shortcuts import render
from rest_framework import viewsets
from .models import category
from .serializers import categorySerializer


class categoryViewSet(viewsets.ModelViewSet):
    queryset=category.objects.all().order_by('name')
    serializer_class=categorySerializer



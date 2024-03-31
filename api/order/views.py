

from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer
from .models import  Order 
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def validete_user_session(id,token):
    user_model =get_user_model()
    try:
        user=user_model.objects.get(pk=id)
        if user.session_token==token:
            return True
        return False
    except user_model.DoesNotExist:
        return False
@csrf_exempt

def add(request,id,token ):
    if not validete_user_session(id,token):
        return JsonResponse({"erorr":"plese re login,'code':'1'"})

    if request.method== "post":
        user_id=id
        transaction_id=request.POST['transaction_id']
        amount=request.POST['amount']
        producte=request.POST['producte']
        total_pro=len(producte.split(','[:-1]))
        UserModel= get_user_model()

        try:
         user= UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return JsonResponse({"error":"user does not exist"})
        
        order=Order(user=user,total_producte=producte,transaction_id=transaction_id,total_amount=amount)
        order.save()
        
        return JsonResponse({"success":True, "error": False,'msg':'Order placed successfully'})

class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all().order_by('id')
    serializer_class=OrderSerializer


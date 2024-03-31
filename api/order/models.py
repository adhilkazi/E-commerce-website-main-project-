from django.db import models
from api.user.models import CustomUser
from api.product.models import product



# Create your models here.


class Order(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)

    product_name=models.CharField(max_length=500)
    total_producte=models.CharField(max_length=500,default=0 )
    transaction_id= models.CharField(max_length = 500,default=0)
    total_amount= models.CharField(max_length=500,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
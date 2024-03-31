
from django.db import models

class category(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

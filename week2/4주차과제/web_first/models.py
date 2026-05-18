# web_first/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100) # 아기사자 이름
   
    
    def __str__(self):
        return self.name
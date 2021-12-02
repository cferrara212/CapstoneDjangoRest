from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class HistoricFact(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=75)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    zip = models.CharField(max_length=5)
    fact = models.CharField(max_length=300)
    
    

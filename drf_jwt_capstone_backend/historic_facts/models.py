from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField
# Create your models here.

class HistoricFact(models.Model):
    user = models.ForeignKey(get_user_model, on_delete=models.PROTECT)
    name = CharField(max_length=75)
    city = CharField(max_length=100)
    

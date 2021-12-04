from rest_framework import serializers
from .models import HistoricFact


class HistorcFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricFact
        fields = ('user', 'name', 'state', 'street', 'city', 'zip', 'fact')
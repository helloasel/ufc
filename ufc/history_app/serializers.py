from rest_framework import serializers
from .models import *

class TurnirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turnir
        fields = ['__all__']

class PeopleTurnirSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleTurnir
        fields = ['__all__']


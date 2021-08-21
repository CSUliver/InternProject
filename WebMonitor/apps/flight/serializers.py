from rest_framework import serializers
from .models import *

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class TakeFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakeFlight
        fields = '__all__'
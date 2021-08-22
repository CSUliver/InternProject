from rest_framework import serializers
from .models import *

class RiskDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfectRisk
        fields = '__all__'

class AlarmDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfectAlarm
        fields = '__all__'
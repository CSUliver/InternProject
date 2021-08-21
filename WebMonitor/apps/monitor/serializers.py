from rest_framework import serializers
from .models import Monitor,MonitorData

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'

class MonitorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorData
        fields = '__all__'
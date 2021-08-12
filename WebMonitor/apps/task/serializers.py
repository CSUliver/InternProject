from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskFinishSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskFinish
        fields = '__all__'
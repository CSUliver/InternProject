from django.shortcuts import render
from .models import *
import time
import json

# Create your views here.

def addLog(*args, **kwargs):
    Logs.objects.create(**kwargs)
    return

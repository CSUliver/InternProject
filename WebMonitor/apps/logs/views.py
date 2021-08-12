from django.shortcuts import render
from .models import *

# Create your views here.

def addLog(*args, **kwargs):
    Logs.objects.create(**kwargs)
    return

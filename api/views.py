from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from dashboard.models import *
from .serializers import *
# Create your views here.

class CuentaView(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

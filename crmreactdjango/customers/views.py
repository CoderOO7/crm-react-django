from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets  
from .models import Customer
from .serializers import CustomerSerializer

# @api_view(['GET', 'POST'])

#viewsets provide implementation of CRUD operation byDefault
class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer  
    queryset = Customer.objects.all()  
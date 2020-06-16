from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from django.contrib.auth.models import User
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class ServiceApiView(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
 

class SchedApiView(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = SchedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
 
    

class UserApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialzier
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'username',]

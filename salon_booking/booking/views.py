from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from django.contrib.auth.models import User
from .serializers import *

# Create your views here.


class ServiceApiView(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = []
    permission_classes = []

class SchedApiView(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = SchedSerializer
    

class UserApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialzier
    authentication_classes = []
    permission_classes = []

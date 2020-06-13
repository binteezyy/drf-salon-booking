from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Services
        fields = ('id', 'name', 'price')


class SchedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'user', 'service', 'sched')


class UserSerialzier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

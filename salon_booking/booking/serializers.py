from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Services
        fields = ('id', 'name', 'price')
        depth = 1


class SchedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'user', 'service', 'sched_date', 'sched_time')

class UserSerialzier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff')
        depth = 1
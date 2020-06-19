from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('services', ServiceApiView)
router.register('schedules', SchedApiView)
router.register('users', UserApiView)

urlpatterns = [
    path("", include(router.urls)),
]

from django.contrib import admin
from .models import *
# Register your models here.


class PostServices(admin.ModelAdmin):
    list_display = ('name', 'price')


class PostSchedule(admin.ModelAdmin):
    list_display = ('user', 'service', 'sched_date', 'sched_time')


admin.site.register(Services, PostServices)
admin.site.register(Schedule, PostSchedule)

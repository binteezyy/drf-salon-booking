from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Services(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f'{self.name} - {self.price} '

    class Meta:
        unique_together = ['name', 'price']


class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.OneToOneField(Services, on_delete=models.CASCADE)
    sched_date = models.DateField()
    sched_time = models.TimeField()

    def __str__(self):
        return f'{self.user.username} - {self.service.name} - {self.sched_date} - {self.sched_time}'

    class Meta:
        unique_together = ['user', 'service', 'sched_date']

import math

from django.db import models
from django.db import models
from datetime import date
from django.db.models import *


# Create your models here.


class Result(models.Model):
    sum = models.FloatField()
    percent = models.FloatField()
    in_candle = models.FloatField()
    settings = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    day_count = models.FloatField()
    config = models.JSONField(max_length=1000, blank=True, )



    def get_absolute_points(self):
        return self.percent * math.sqrt(self.sum)/self.day_count

class MixResult(models.Model):

    config1 = models.ForeignKey(Result, related_name='res1', on_delete=models.CASCADE,  blank=True)
    config2 = models.ForeignKey(Result, related_name='res2', on_delete=models.CASCADE,  blank=True)
    config3 = models.ForeignKey(Result, related_name='res3', on_delete=models.CASCADE,  blank=True)

    sum = models.FloatField()
    percent = models.FloatField()
    in_candle = models.FloatField()
    settings = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    day_count = models.FloatField()

    def get_absolute_points(self):
        return self.percent * math.sqrt(self.sum)/self.day_count





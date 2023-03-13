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
    settings = models.CharField(max_length=2000)
    date_added = models.DateTimeField(auto_now_add=True)
    day_count = models.FloatField()
    config = models.JSONField(max_length=2000, blank=True, )
    percent_mult = models.FloatField()
    method = models.CharField(max_length=200)
    version = models.CharField(max_length=200)

    def get_absolute_points( self ):
        return self.percent_mult* math.sqrt(self.sum)


class MixResult(models.Model):
    config1 = models.ForeignKey(Result, related_name='res1', on_delete=models.CASCADE, blank=True)
    config2 = models.ForeignKey(Result, related_name='res2', on_delete=models.CASCADE, blank=True)
    config3 = models.ForeignKey(Result, related_name='res3', on_delete=models.CASCADE, blank=True)

    sum = models.FloatField()
    percent = models.FloatField()
    percent_mult = models.FloatField()
    in_candle = models.FloatField()
    settings = models.CharField(max_length=1500)
    date_added = models.DateTimeField(auto_now_add=True)
    day_count = models.FloatField()
    method = models.CharField(max_length=100)

    def get_absolute_points( self ):
        return self.percent_mult * math.sqrt(self.sum)

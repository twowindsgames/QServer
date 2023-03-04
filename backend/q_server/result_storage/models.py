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
    settings = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-percent',)



    def get_absolute_points( self ):
        return self.percent*self.percent*math.sqrt(self.in_candle)*math.sqrt(self.sum)
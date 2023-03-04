from rest_framework import serializers

from .models import *


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = (
            "id",
            "sum",
            "day_count",
            "percent",
            "in_candle",
            "settings",
            "date_added",
            "get_absolute_points"
        )

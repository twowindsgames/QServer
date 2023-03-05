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
            "config",
            "get_absolute_points"
        )

class MixResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MixResult
        fields = (
            "id",
            "config1",
            "config2",
            "config3",
            "sum",
            "day_count",
            "percent",
            "in_candle",
            "settings",
            "date_added",
            "get_absolute_points",
        )

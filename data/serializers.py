from rest_framework import serializers
from .models import CurrenciesData


class CurrenciesDataSerializer(serializers.Serializer):

    ratio_of_dollar_on_euro = serializers.FloatField()
    last_modified = serializers.DateTimeField()
    currency = serializers.CharField()
    amount = serializers.IntegerField()


class RatioSerializer(serializers.Serializer):
    ratio_of_dollar_on_euro = serializers.FloatField()
    last_modified = serializers.DateTimeField()

from rest_framework import serializers
from .models import CurrenciesData


class CurrenciesDataSerializer(serializers.Serializer):
    class Meta:
        model = CurrenciesData
        fields = ("currency", "amount", "ratio_of_dollar_on_euro", "last_modified")


class RatioSerializer(serializers.Serializer):
    dictionary = serializers.DictField(child=serializers.CharField())

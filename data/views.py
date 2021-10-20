from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from data.serializers import CurrenciesDataSerializer, RatioSerializer
from django.http import HttpResponse

from .models import CurrenciesData


def home(request):
    # print(CurrenciesData.objects.values("ratio_of_dollar_on_euro", "last_modified"))
    # # ser_data = RatioSerializer(
    # #     CurrenciesData.objects.values("ratio_of_dollar_on_euro", "last_modified"),
    # #     many=True,
    # # )
    # # print(ser_data)
    # print(CurrenciesData.objects.get_daily_usd_amount())
    print(CurrenciesData.objects.all().values('id'))
    print(CurrenciesData.objects.filter(currency='EURO').get().amount)
    # print(CurrenciesData.objects.filter(id=2).values_list('amount')[0][0])

    return HttpResponse("jo")


@api_view()
def current_usd(request):
    current_usd_amount = CurrenciesData.objects.get_current_usd_amount()
    ser_data = CurrenciesDataSerializer(current_usd_amount)
    return Response(ser_data.data, status=status.HTTP_200_OK)


@api_view()
def current_euro(request):
    current_euro_amount = CurrenciesData.objects.get_current_euro_amount()
    ser_data = CurrenciesDataSerializer(current_euro_amount)
    return Response(ser_data.data, status=status.HTTP_200_OK)


@api_view()
def history_usd(request):
    daily_usd_amount = CurrenciesData.objects.get_daily_usd_amount()
    ser_data = CurrenciesDataSerializer(daily_usd_amount, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)


@api_view()
def history_euro(request):
    daily_euro_amount = CurrenciesData.objects.get_daily_euro_amount()
    ser_data = CurrenciesDataSerializer(daily_euro_amount, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)


@api_view()
def history_ratio(request):
    daily_ratio = CurrenciesData.objects.values(
        "ratio_of_dollar_on_euro", "last_modified"
    )
    ser_data = RatioSerializer(daily_ratio, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)

import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import CurrenciesData


class CurrenciesDataType(DjangoObjectType):
    class Meta:
        model = CurrenciesData


class CurrenciesDataQuery(ObjectType):

    all_info = graphene.List(CurrenciesDataType)
    current_amount_currency = graphene.Field(
        CurrenciesDataType, currency=graphene.String()
    )
    daily_amount_currency = graphene.List(
        CurrenciesDataType, currency=graphene.String()
    )

    def resolve_all_info(parent, info, **kwargs):
        return CurrenciesData.objects.all()

    def resolve_current_amount_currency(parent, info, **kwargs):
        currency = kwargs.get("currency")
        if currency is not None:
            return CurrenciesData.objects.get_current_amount(currency=currency)
        return None

    def resolve_daily_amount_currency(parent, info, **kwargs):
        currency = kwargs.get("currency")
        if currency is not None:
            return CurrenciesData.objects.get_daily_amount(currency=currency)
        return None

from django.db import models
import enum


class CurrenciesDataManager(models.Manager):
    def get_current_amount(self, currency):
        return self.filter(currency=currency).last()

    def get_daily_amount(self, currency):
        return self.filter(currency=currency)


class CurrenciesData(models.Model):
    class CurrencyType(enum.IntEnum):
        USD = 1
        EURO = 2

        @classmethod
        def choices(cls):
            return [(key.name, key.value) for key in cls]

        @classmethod
        def get_currency(cls, value):
            return cls(value).name

    currency = models.CharField(
        max_length=100, choices=CurrencyType.choices(), default=CurrencyType.USD.value
    )
    amount = models.IntegerField(max_length=50)
    ratio_of_dollar_on_euro = models.FloatField(max_length=100, default=0.0)
    last_modified = models.DateTimeField(auto_now=True)

    objects = CurrenciesDataManager()

    def __str__(self):
        return f"{self.currency} at {self.last_modified} : {self.amount}"

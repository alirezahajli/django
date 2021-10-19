from django.db import models
import enum


class CurrenciesData (models.Model):

    class CurrencyType(enum.IntEnum):
        DOLLAR = 1
        EURO = 2

        @classmethod
        def choices(cls):
            return [(key.name, key.value) for key in cls]

        @classmethod
        def get_currency(cls, value):
            return cls(value).name

    currency = models.CharField(
        max_length=100,
        choices=CurrencyType.choices(),
        default=CurrencyType.DOLLAR.value)
    amount = models.IntegerField(max_length=50)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.currency} at {self.last_modified}"

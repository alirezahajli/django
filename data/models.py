from django.db import models
import enum


class CurrenciesDataManager(models.Manager):
    def get_current_amount(self, currency):
        return self.filter(currency=currency).last()

    def get_daily_amount(self, currency):
        return self.filter(currency=currency)

    def get_random_data(self, number):
        return self.raw(
            f"SELECT * FROM data_currenciesdata WHERE id IN (SELECT id FROM data_currenciesdata TABLESAMPLE system_rows({number}));"
        )


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
        max_length=40, choices=CurrencyType.choices(), default=CurrencyType.USD.value
    )
    amount = models.IntegerField()
    last_modified = models.DateTimeField(auto_now=True)
    ratio_of_dollar_on_euro = models.FloatField(max_length=100, default=0.0)

    objects = CurrenciesDataManager()

    def __str__(self):
        return f"{self.currency} at {self.last_modified} : {self.amount}"

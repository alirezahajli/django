import enum


class Currency(enum.IntEnum):
    DOLLAR = 1
    EURO = 2

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]

    @classmethod
    def get_currency(cls, value):
        return cls(value).name

# c = Currency()

print(Currency.choices())
import requests
from decouple import config


class GetData:
    def __init__(self) -> None:
        pass

    def get_last_amount(self, currency: str) -> int:
        spilited_contenet = self.__get_request_content(currency)
        _index = None
        for indx, spilit in enumerate(spilited_contenet, start=0):
            if "info.last_trade.PDrCotVal" in spilit:
                _index = indx
                break
        last_currency_amount = spilited_contenet[_index].split("<")
        amount = int(last_currency_amount[0].split(">")[1].replace(",", ""))
        return amount

    def __get_request_content(self, currency: str) -> list:
        urls = {
            "usd": config("USD_PATH"),
            "euro": config("EURO_PATH"),
        }
        res = requests.get(urls[currency])

        return res.content.decode("utf-8").split()

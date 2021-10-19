import requests


class GetData:
    def __init__(self) -> None:
        pass

    def __get_request_content(self, currency):
        urls = {
            "usd": "https://www.tgju.org/profile/price_dollar_rl",
            "euro": "https://www.tgju.org/profile/price_eur",
        }
        request = requests.get(urls[currency])
        get_amount_from_content = request.content.decode("utf-8").split()

        return get_amount_from_content

    def get_last_amount(self, currency):
        spilited_contenet = self.__get_request_content(currency)
        _index = None
        for indx, spilit in enumerate(spilited_contenet, start=0):
            if "info.last_trade.PDrCotVal" in spilit:
                _index = indx
                break
        last_currency_amount = spilited_contenet[_index].split("<")

        return last_currency_amount[0].split(">")

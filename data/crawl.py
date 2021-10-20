import requests


class GetData:
    def __init__(self) -> None:
        pass

    def __get_request_content(self, currency) -> list:
        urls = {
            "usd": "https://www.tgju.org/profile/price_dollar_rl",
            "euro": "https://www.tgju.org/profile/price_eur",
        }
        request = requests.get(urls[currency])
        get_amount_from_content = request.content.decode("utf-8").split()

        return get_amount_from_content

    def get_last_amount(self, currency) -> int:
        spilited_contenet = self.__get_request_content(currency)
        _index = None
        for indx, spilit in enumerate(spilited_contenet, start=0):
            if "info.last_trade.PDrCotVal" in spilit:
                _index = indx
                break
        last_currency_amount = spilited_contenet[_index].split("<")
        amount = int(last_currency_amount[0].split(">")[1].replace(',', ''))
        return amount

import httpx
from decouple import config


def get_last_amount(spilited_contenet: list) -> int:
    _index = None
    for indx, spilit in enumerate(spilited_contenet):
        if "info.last_trade.PDrCotVal" in spilit:
            _index = indx
            break
    last_currency_amount = spilited_contenet[_index].split("<")
    return int(last_currency_amount[0].split(">")[1].replace(",", ""))


def get_page_content(currency: str, client: httpx.Client) -> list:
    urls = {"usd": config("USD_PATH"), "euro": config("EURO_PATH")}
    res = client.get(urls[currency])
    return res.content.decode("utf-8").split()

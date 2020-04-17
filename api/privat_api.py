import requests
from api import _Api


class Api(_Api):
    def __init__(self):
        super().__init__("PrivatApi")

    def _updata_rate(self, xrate):
        rate = self._get_privat_rate(xrate.from_currency)
        return rate

    def _get_privat_rate(self, from_currency):
        response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11",
                                method="get")
        response_json = response.json()
        self.log.debug("Privat response: %s" % response_json)
        rate = self._find_rate(response_json, from_currency)

        return rate

    def _find_rate(self, response_data, from_currency):
        pr_valute_map = {840: "USD"}
        currency_pr_alias = pr_valute_map[from_currency]
        for e in response_data:
            if e["ccy"] == currency_pr_alias:
                return float(e["sale"])

        raise ValueError("Invalid Privat response: USD not found ")

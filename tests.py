import unittest
import json
from unittest.mock import patch

import xmltodict
import requests

import models
import api


def get_privat_response(*args, **kwargs):
    print("get_privat_response")

    class Response:
        def __init__(self, response):
            self.text = json.dump(response)

        def json(self):
            return json.loads(self.text)
    return Response([{"ccy": "USD", "base_ccy": "UAH", "sale": "30.0"}])


class Test(unittest.TestCase):

    # @unittest.skip("Пропускаем тест")
    # def setUp(self):
    #     models.init_db()
    #
    # @unittest.skip("Пропускаем тест")
    # def test_privat_usd(self):
    #
    #     xrate = models.XRate.get(from_currency=840, to_currency=980)
    #     updated_before = xrate.updated
    #     self.assertEqual(xrate.rate, 1.0)
    #
    #     api.update_rate(840, 980)
    #
    #     xrate = models.XRate.get(from_currency=840, to_currency=980)
    #     updated_after = xrate.updated
    #
    #     self.assertGreater(xrate.rate, 25)
    #     self.assertGreater(updated_after, updated_before)
    #
    #     api_log = models.ApiLog.select().order_by(models.ApiLog.created.desc()).first()
    #
    #     self.assertIsNotNone(api_log)
    #     self.assertEqual(api_log.request_url, "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")
    #     self.assertIsNotNone(api_log.response_text)
    #
    #     self.assertIn('{"ccy": "USD", "base_ccy": "UAH",', api_log.response_text)
    #
    # @unittest.skip("Пропускаем тест")
    # def test_privat_btc(self):
    #     xrate = models.XRate.get(from_currency=1000, to_currency=840)
    #     updated_before = xrate.updated
    #     self.assertEqual(xrate.rate, 1.0)
    #
    #     api.update_rate(1000, 840)
    #
    #     xrate = models.XRate.get(from_currency=1000, to_currency=840)
    #     updated_after = xrate.updated
    #
    #     self.assertGreater(updated_after, updated_before)
    #     self.assertGreater(xrate.rate, 5000)
    #
    # @unittest.skip("Пропускаем тест")
    # def test_cbr(self):
    #     xrate = models.XRate.get(from_currency=840, to_currency=643)
    #     updated_before = xrate.updated
    #     self.assertEqual(xrate.rate, 1.0)
    #
    #     api.update_rate(840, 643)
    #
    #     xrate = models.XRate.get(from_currency=840, to_currency=643)
    #     update_after = xrate.updated
    #
    #     self.assertGreater(xrate.rate, 60)
    #     self.assertGreater(update_after, updated_before)
    #
    #     api_log = models.ApiLog.select().order_by(models.ApiLog.created.desc()).first()
    #
    #     self.assertIsNotNone(api_log)
    #     self.assertEqual(api_log.request_url, "http://www.cbr.ru/scripts/XML_daily.asp")
    #     self.assertIsNotNone(api_log.response_text)
    #     self.assertIn("<NumCode>840</NumCode>", api_log.response_text)
    #
    # @unittest.skip("Пропускаем тест")
    # @patch('api._Api._send', new=get_privat_response)
    # def test_privat_mock(self):
    #
    #     xrate = models.XRate.get(id=1)
    #     updated_before = xrate.updated
    #     self.assertEqual(xrate.rate, 1.0)
    #
    #     privat_api.Api.updata_rate(840, 980)
    #
    #     xrate = models.XRate.get(id=1)
    #     updated_after = xrate.updated
    #
    #     self.assertGreater(updated_after, updated_before)
    #     self.assertEqual(xrate.rate, 30)
    #
    #     api_log = models.ApiLog.select().order_by(models.ApiLog.created.desc()).first()
    #
    #     self.assertIsNotNone(api_log)
    #     self.assertEqual(api_log.request_url, "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")
    #     self.assertIsNotNone(api_log.response_text)
    #
    #     self.assertIn('[{"ccy": "USD", "base_ccy": "UAH", "sale": "30.0"}]', api_log.response_text)
    #
    # @unittest.skip("Пропускаем тест")
    # def test_cryrtonator_uah(self):
    #     xrate = models.XRate.get(from_currency=1000, to_currency=980)
    #     updated_before = xrate.updated
    #     self.assertEqual(xrate.rate, 1.0)
    #
    #     cryptonator_api.Api().updata_rate(1000, 980)
    #
    #     xrate = models.XRate.get(from_currency=1000, to_currency=980)
    #     update_after = xrate.updated
    #
    #     self.assertGreater(xrate.rate, 100000)
    #     self.assertGreater(update_after, updated_before)

    def test_xml_api(self):
        r = requests.get("http://localhost:5000/api/xrates/xml")
        self.assertIn("<xrates>", r.text)
        print(r.text)
        # xml_rates = xmltodict.parse(r.text)
        # self.assertIn("xrates", xml_rates)
        # self.assertIsInstance(xml_rates["xrates"]["xrate"], list)
        # self.assertEqual(len(xml_rates["xrates"]["xrate"]), 5)

    # def test_json_api(self):
    #     r = requests.get("http://localhost:5000/api/xrates/json")
    #     json_rates = r.json()
    #     self.assertIsInstance(json_rates, list)
    #     self.assertEqual(len(json_rates), 5)
    #     for rate in json_rates:
    #         self.assertIn("from", rate)
    #         self.assertIn("to", rate)
    #         self.assertIn("rate", rate)
    #
    # def test_json_api_uah(self):
    #     r = requests.get("http://localhost:5000/api/xrates/json?to_currency=980")
    #     json_rates = r.json()
    #     self.assertIsInstance(json_rates, list)
    #     self.assertEqual(len(json_rates), 2)


if __name__ == '__main__':
    unittest.main()

import unittest
import json
from unittest.mock import patch

import models
import api.privat_api as privat_api
import api.cbr_api as cbr_api


# def get_privat_response(*args, **kwargs):
#     class Response:
#         def __init__(self, response):
#             self.text = json.dump(response)
#
#         def json(self):
#             return json.loads(self.text)
#     return Response([{"ccy": "USD", "base_ccy": "UAH", "sale": "30.0"}])


class Test(unittest.TestCase):
    def setUp(self):
        models.init_db()

    # def test_privat_usd(self):
    #     xrate = models.XRate.get(from_currency=840, to_currency=980)
    #     updated_before = xrate.updated
    #     self.assertEqual(xrate.rate, 1.0)
    #
    #     privat_api.Api().updata_rate(840, 980)
    #
    #     xrate = models.XRate.get(from_currency=840, to_currency=980)
    #     updated_after = xrate.updated
    #
    #     self.assertGreater(updated_after, updated_before)
    #     self.assertGreater(xrate.rate, 25)
    #
    #     # api_log = models.ApiLog.select().order_by(models.ApiLog.created.desc()).first()
    #     #
    #     # self.assertIsNotNone(api_log)
    #     # self.assertEqual(api_log.request_url, "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")
    #     # self.assertIsNotNone(api_log.response_text)
    #     #
    #     # self.assertIn('{"ccy": "USD", "base_ccy": "UAH", ', api_log.response_text)

    # def test_privat_btc(self):
    #     xrate = models.XRate.get(from_currency=1000, to_currency=840)
    #     updated_before = xrate.updated
    #     self.assertEqual(xrate.rate, 1.0)
    #
    #     privat_api.Api().updata_rate(1000, 840)
    #
    #     xrate = models.XRate.get(from_currency=1000, to_currency=840)
    #     updated_after = xrate.updated
    #
    #     self.assertGreater(updated_after, updated_before)
    #     self.assertGreater(xrate.rate, 5000)
    #
    def test_cbr(self):
        xrate = models.XRate.get(from_currency=840, to_currency=643)
        updated_before = xrate.updated
        self.assertEqual(xrate.rate, 1.0)

        cbr_api.Api().updata_rate(840, 643)

        xrate = models.XRate.get(from_currency=840, to_currency=643)
        update_after = xrate.updated

        self.assertGreater(xrate.rate, 60)
        self.assertGreater(update_after, updated_before)

        # api_log = models.ApiLog.select().order_by(models.ApiLog.created.desc()).first()
        #
        # self.assertIsNotNone(api_log)
        # self.assertEqual(api_log.request_url, "http://www.cbr.ru/scripts/XML_daily.asp")
        # self.assertIsNotNone(api_log.response_text)
        # self.assertIn("<NumCode>840</NumCode>", api_log.response_text)

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


if __name__ == '__main__':
    unittest.main()

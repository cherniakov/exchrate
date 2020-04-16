import unittest

import test_api
import models
import privat_api
import cbr_api


class Test(unittest.TestCase):
    def setUp(self):
        models.init_db()

    def test_main(self):
        xrate = models.XRate.get(id=1)
        self.assertEqual(xrate.rate, 1.0)
        test_api.update_xrates(840, 980)
        xrate = models.XRate.get(id=1)
        self.assertEqual(xrate.rate, 1.01)

    def test_privat(self):
        xrate = models.XRate.get(id=1)
        update_before = xrate.updated
        self.assertEqual(xrate.rate, 1.0)
        privat_api.updata_xrates(840, 980)
        xrate = models.XRate.get(id=1)
        update_after = xrate.updated

        self.assertGreater(xrate.rate, 25)
        self.assertGreater(update_after, update_before)

    def test_cbr(self):
        xrate = models.XRate.get(from_currency=840, to_currency=643)
        update_before = xrate.updated
        self.assertEqual(xrate.rate, 1.0)
        cbr_api.updata_xrates(840, 643)
        xrate = models.XRate.get(from_currency=840, to_currency=643)
        update_after = xrate.updated

        self.assertGreater(xrate.rate, 60)
        self.assertGreater(update_after, update_before)


if __name__ == '__main__':
    unittest.main()

import unittest
from src.CryptoCurrency import Cryptocurrency


class MyTestCase(unittest.TestCase):
    def test_GetBtcPrice(self):
        price = float(Cryptocurrency().get_btc_price())
        self.assertTrue(0 <= price <= 10 ** 8)

    def test_GetBCHPrice(self):
        price = float(Cryptocurrency().get_bch_price())
        self.assertTrue(0 <= price <= 10 ** 6)

    def test_GetEOSPrice(self):
        price = float(Cryptocurrency().get_eos_price())
        self.assertTrue(0 <= price <= 10 ** 5)

import unittest
from datetime import datetime
from portfolio import Stock, Portfolio, check_stock_exists, check_date

class TestStock(unittest.TestCase):

    def test_check_stock_exists(self):
        self.assertTrue(check_stock_exists("AAPL"))
        self.assertFalse(check_stock_exists("INVALID"))

    def test_check_date(self):
        self.assertTrue(check_date("2022-01-01"))
        self.assertFalse(check_date("2022-01-32"))
        self.assertFalse(check_date("2022-13-01"))
        self.assertFalse(check_date("2022-01"))

    def test_getPrice(self):
        stock = Stock("AAPL")
        price = stock.getPrice("2022-01-01")
        self.assertIsInstance(price, float)

class TestPortfolio(unittest.TestCase):

    def setUp(self):
        self.portfolio = Portfolio()
        self.stock1 = Stock("AAPL")
        self.stock2 = Stock("GOOGL")
        self.portfolio.addStock(self.stock1)
        self.portfolio.addStock(self.stock2)

    def test_addStock(self):
        self.assertEqual(len(self.portfolio.stocks), 2)

    def test_getProfit(self):
        start_date = "2022-01-01"
        end_date = "2022-01-31"
        profit = self.portfolio.getProfit(start_date, end_date)
        self.assertIsInstance(profit, float)

    def test_getAnnualizedReturn(self):
        start_date = "2022-01-01"
        end_date = "2022-12-31"
        annualized_return = self.portfolio.getAnnualizedReturn(start_date, end_date)
        self.assertIsInstance(annualized_return, float)

if __name__ == '__main__':
    unittest.main()
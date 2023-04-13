from datetime import datetime

import unittest
from datetime import date
from engine.sternman_engine import SternmanEngine
from engine.palindrome import Palindrome


class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.engine = Palindrome()

    def test_needs_service_past_threshold(self):
        self.engine.last_service_date = date.today().replace(year=date.today().year - 5)
        self.assertTrue(self.engine.needs_service())

    def test_needs_service_within_threshold(self):
        self.engine.last_service_date = date.today().replace(year=date.today().year - 3)
        self.assertFalse(self.engine.needs_service())

    def test_needs_service_engine_should_be_serviced(self):
        self.engine.last_service_date = date.today().replace(year=date.today().year - 2)
        self.engine.service_interval = 1
        self.assertTrue(self.engine.needs_service())

    def test_needs_service_engine_should_not_be_serviced(self):
        self.engine.last_service_date = date.today().replace(year=date.today().year - 2)
        self.engine.service_interval = 3
        self.assertFalse(self.engine.needs_service())


if __name__ == '__main__':
    unittest.main()


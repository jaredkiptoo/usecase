import unittest
from datetime import date, timedelta
from unittest.mock import patch, MagicMock
from engine.willoughby_engine import WilloughbyEngine
from engine.rorschach import Rorschach


class TestRorschach(unittest.TestCase):

    def setUp(self):
        self.rorschach = Rorschach()
        self.today = date.today()

    def test_needs_service_last_service_date_more_than_4_years_ago(self):
        self.rorschach.last_service_date = self.today - timedelta(days=1460)  # 4 years and 1 day ago
        self.assertTrue(self.rorschach.needs_service())

    def test_needs_service_last_service_date_less_than_4_years_ago(self):
        self.rorschach.last_service_date = self.today - timedelta(days=1459)  # 3 years and 364 days ago
        self.assertFalse(self.rorschach.needs_service())

    def test_needs_service_engine_should_be_serviced(self):
        self.rorschach.last_service_date = self.today - timedelta(days=1460)  # 4 years and 1 day ago
        self.rorschach.engine_should_be_serviced = MagicMock(return_value=True)
        self.assertTrue(self.rorschach.needs_service())

    @patch('engine.rorschach.datetime')
    def test_needs_service_today_less_than_service_threshold_date(self, mock_datetime):
        mock_datetime.today.return_value = self.today
        self.rorschach.last_service_date = self.today - timedelta(days=1460)  # 4 years and 1 day ago
        service_threshold_date = self.rorschach.last_service_date.replace(year=self.rorschach.last_service_date.year + 4)
        mock_datetime.today.return_value = service_threshold_date - timedelta(days=1)
        self.assertFalse(self.rorschach.needs_service())

    @patch('engine.rorschach.datetime')
    def test_needs_service_today_greater_than_service_threshold_date(self, mock_datetime):
        mock_datetime.today.return_value = self.today
        self.rorschach.last_service_date = self.today - timedelta(days=1460)  # 4 years and 1 day ago
        service_threshold_date = self.rorschach.last_service_date.replace(year=self.rorschach.last_service_date.year + 4)
        mock_datetime.today.return_value = service_threshold_date + timedelta(days=1)
        self.assertTrue(self.rorschach.needs_service())


if __name__ == '__main__':
    unittest.main()


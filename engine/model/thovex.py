from datetime import date, timedelta
import unittest
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def setUp(self):
        self.last_service_date = date.today() - timedelta(days=365)  # 1 year ago
        self.current_mileage = 45000
        self.last_service_mileage = 15000
        self.engine = CapuletEngine(self.last_service_date, self.current_mileage, self.last_service_mileage)

    def test_engine_should_be_serviced(self):
        # Test that engine should be serviced when mileage threshold is exceeded
        self.engine.current_mileage = 50000
        self.assertTrue(self.engine.engine_should_be_serviced())

        # Test that engine should not be serviced when mileage threshold is not exceeded
        self.engine.current_mileage = 25000
        self.assertFalse(self.engine.engine_should_be_serviced())

    def test_needs_service(self):
        # Test that engine needs service when last service date is over 4 years ago
        self.engine.last_service_date = date.today() - timedelta(days=1461)  # 4 years + 1 day ago
        self.assertTrue(self.engine.needs_service())

        # Test that engine needs service when mileage threshold is exceeded
        self.engine.last_service_date = date.today() - timedelta(days=300)  # 300 days ago
        self.engine.current_mileage = 50000
        self.assertTrue(self.engine.needs_service())

        # Test that engine does not need service when neither condition is met
        self.engine.last_service_date = date.today() - timedelta(days=180)  # 180 days ago
        self.engine.current_mileage = 25000
        self.assertFalse(self.engine.needs_service())

if __name__ == '__main__':
    unittest.main()

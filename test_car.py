import unittest
from datetime import datetime
from carFactory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]

        car = CarFactory.create_calliope(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]

        car = CarFactory.create_calliope(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_calliope(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_calliope(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.1, 0.4, 1.0, 0.8]

        car = CarFactory.create_calliope(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.8, 0.8, 0.8, 0.8]

        car = CarFactory.create_calliope(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_glissade(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_glissade(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001 
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_glissade(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_glissade(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertFalse(car.needs_service())


    def test_tire_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.8, 0.8, 0.8, 0.8]

        car = CarFactory.create_glissade(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.0, 0.4, 0.2, 1.0]

        car = CarFactory.create_glissade(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        warning_light_is_on = False
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_palindrome(CarFactory, today, last_service_date, warning_light_is_on, sensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        warning_light_is_on = False
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_palindrome(CarFactory, today, last_service_date, warning_light_is_on, sensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_palindrome(CarFactory, today, last_service_date, warning_light_is_on, sensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_palindrome(CarFactory, today, last_service_date, warning_light_is_on, sensors)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        current_mileage = 0
        last_service_mileage = 0
        sensors = [1, 1, 1, 1]

        car = CarFactory.create_palindrome(CarFactory, today, last_service_date, warning_light_is_on, sensors)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.6, 0.8, 0.1, 0.8]

        car = CarFactory.create_palindrome(CarFactory, today, last_service_date, warning_light_is_on, sensors)
        self.assertFalse(car.needs_service())



class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_rorschach(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_rorschach(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_rorschach(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_rorschach(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0, 1.0, 1.0, 1.0]

        car = CarFactory.create_rorschach(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.2, 0.7, 1, 1]

        car = CarFactory.create_rorschach(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertFalse(car.needs_service())



class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_thovex(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_thovex(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_thovex(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        sensors = [0.0, 0.0, 0.0, 0.0]
        car = CarFactory.create_thovex(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.1, 0.8, 1.0, 0.9]

        car = CarFactory.create_thovex(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.8999, 0.89, 0.89, 0.8]

        car = CarFactory.create_thovex(CarFactory, today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertFalse(car.needs_service())



if __name__ == '__main__':
    unittest.main()

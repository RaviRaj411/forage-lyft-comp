import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoprimeTire

from car_factory import CarFactory
from utils import add_years_to_date


## task 4 ##
class testCarriganTires(unittest.TestCase):
    def test_tire_should_be_services(self):
        worn_tire = [0.69,0.54,0.76,0.96]
        carriganTire = CarriganTire(worn_tire)
        self.assertTrue(carriganTire.needs_service())

    def test_tire_should_not_be_services(self):
        worn_tire = [0.69,0.54,0.76,0.86]
        carriganTire = CarriganTire(worn_tire)
        self.assertFalse(carriganTire.needs_service())

class testOctoprimeTires(unittest.TestCase):
    def test_tire_should_be_services(self):
        worn_tire = [0.69,0.84,0.86,0.86]
        octoprimeTire = OctoprimeTire(worn_tire)
        self.assertTrue(octoprimeTire.needs_service())

    def test_tire_should_not_be_services(self):
        worn_tire = [0.3,0.4,0.6,0.6]
        octoprimeTire = OctoprimeTire(worn_tire)
        self.assertFalse(octoprimeTire.needs_service())



## task 3  ##
# new test cases for individual batteries and engines
class testSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today,-4)
        spindlerBattery = SpindlerBattery(today, last_service_date)

        self.assertTrue(spindlerBattery.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today,-2)
        spindlerBattery = SpindlerBattery(today, last_service_date)

        self.assertFalse(spindlerBattery.needs_service())

        
class testNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today,-5)
        nubbinBattery = NubbinBattery(today, last_service_date)
        self.assertTrue(nubbinBattery.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today,-3)
        nubbinBattery = NubbinBattery(today, last_service_date)
        self.assertFalse(nubbinBattery.needs_service())



class testCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capuletEngine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capuletEngine.needs_service())

class testSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        sternmanEngine = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternmanEngine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        sternmanEngine = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternmanEngine.needs_service())

class testWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughbyEngine.needs_service())


    def test_engine_should_not_be_serviced(self):
        current_mileage = 6000
        last_service_mileage = 0
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughbyEngine.needs_service())




# modified old test cases for each car model  
class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()

        last_service_date = add_years_to_date(today,-4)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today,-2)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today=last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today=last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today,-4)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()

        last_service_date = add_years_to_date(today,-2)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today= last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today= last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)

        self.assertFalse(car.needs_service())

  

class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today,-4)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today,-2)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today=last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today=last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today,-5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today,-3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today= last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today= last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today,-5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = add_years_to_date(today,-3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today= last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today= last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())



if __name__ == '__main__':
    unittest.main()

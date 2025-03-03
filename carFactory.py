from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from car import Car

class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, sensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTire(sensors)
        return Car(engine, battery, tires)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, sensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTire(sensors)
        return Car(engine, battery, tires)

    def create_palindrome(self, current_date, last_service_date, warning_light_on, sensors):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTire(sensors)
        return Car(engine, battery, tires)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, sensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTire(sensors)
        return Car(engine, battery, tires)
        
    def create_thovex(self, current_date, last_service_date,current_mileage, last_service_mileage, sensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTire(sensors)
        return Car(engine, battery, tires)


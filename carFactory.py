from engine import capulet_engine
from engine import willoughby_engine
from engine import sternman_engine
from battery import spindler_battery
from battery import nubbin_battery
from car import Car

class CarFactory():
    def create_calliope(self, current_date, last_service_date, date, current_mileage, last_service_mileage):
        Car(self.last_service_date, capulet_engine, spindler_battery)

    def create_glissade(self, current_date, last_service_date, date, current_mileage, last_service_mileage):
        Car(self.last_service_date, willoughby_engine, spindler_battery)

    def create_palindrome(self, current_date, last_service_date, date, current_mileage, last_service_mileage):
        Car(self.last_service_date, sternman_engine, nubbin_battery)

    def create_rorschach(self, current_date, last_service_date, date, current_mileage, last_service_mileage):
        Car(self.last_service_date, willoughby_engine, nubbin_battery)

    def create_thovex(self, current_date, last_service_date, date, current_mileage, last_service_mileage):
        Car(self.last_service_date, capulet_engine, nubbin_battery)


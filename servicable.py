from car import Car

class Servicable(Car):
    def needs_service(self):
        return super().needs_service()


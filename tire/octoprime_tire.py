from tire import tire

class OctoprimeTire(tire.Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        sum = 0
        for sensor in self.sensors:
            sum = sum + sensor
        if (sum >= 3):
            return True
        return False
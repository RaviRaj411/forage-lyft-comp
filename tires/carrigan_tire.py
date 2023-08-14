from tires.tire import Tire
class CarriganTire(Tire):
    def __init__(self, tire_wear):
       self.tire_wear=tire_wear
    def needs_service(self):
        return any(num > 0.9 for num in self.tire_wear)
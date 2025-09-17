#  Run this file to see the output
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    def drive(self):
        print("Driving")
class ElectricCar(Car):
    def __init__(self, color, model, battery):
        super().__init__(color, model)
        self.battery = battery
    def drive(self):
        print("Driving with electric power")
class HybridCar(Car):
    def __init__(self, color, model, battery):
        super().__init__(color, model)
        self.battery = battery
    def drive(self):
        print("Driving with hybrid power")

electric_car = ElectricCar("red", "2020", "1000")
electric_car.drive()
hybrid_car = HybridCar("blue", "2020", "1000")
hybrid_car.drive()

# Ouput:
# Driving with electric power
# Driving with hybrid power

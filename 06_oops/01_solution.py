class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car =+ 1

    def get_brand(self):
        return self.__brand
        
    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "run on petrol or disel"

class ElectricCar(Car): 
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def fuel_type(self):
            return "Electric charge"

my_eleCar = ElectricCar("Tata", "punch", "40kw")
print(my_eleCar.get_brand())
print(my_eleCar.fuel_type())
print(my_eleCar.total_car)


safari = Car("tata","safari")
print(safari.fuel_type())
print(safari.total_car)


        
# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_car1 = Car("Maruti", "eartica")
# print(my_car1.brand)
# print(my_car1.model)

# print(my_car1.full_name())
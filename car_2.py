class Car:


    wheels = 4
    country_of_manufacture = "UK"

    def __init__(self,type,brand):
        self.type = type
        self.brand = brand


model_y = Car("Sedan", "Tesla")
prius = Car("Sedan", "Toyota")
defender = Car("SUV", "Land_Rover")

print(model_y.type)
print(prius.brand)
print(defender.type)

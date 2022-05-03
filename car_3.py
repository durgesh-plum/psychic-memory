class Car:

    def __init__(self, make, speed):
        self.make = make
        self.speed = speed

    def accelerate(self):
        self.speed = self.speed + 5

    def brake(self):
        self.speed = self.speed - 5

    def get_speed(self):
        return self.speed

if __name__ == '__main__':

    suv = Car('Tesla', 100)
    print(suv.get_speed())

    suv.accelerate()
    print(suv.get_speed())

    suv.accelerate()
    print(suv.get_speed())

    suv.accelerate()
    print(suv.get_speed())

    suv.accelerate()
    print(suv.get_speed())

    suv.accelerate()
    print(suv.get_speed())

    print(suv.get_speed())
    print(suv.get_speed())

    suv.brake()
    suv.brake()
    print(suv.get_speed())

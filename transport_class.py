class Transport:

    def __init__(self, make, brake,speed,accelerate):
        self.make = make
        self.speed = speed
        self.brake = brake
        self.accelerate = accelerate

    def set_make(self, make):
        self.make = make

    def set_accelerate(self, accelerate):
        self.accelerate = accelerate

    def set_brake(self, brake):
        self.brake = brake

    def accelerate(self):
        self.speed +=5

    def brake(self):
        self.speed -=5

    def get_speed(self):
        return self.speed

from transport_class import Transport

class Car(Transport):
    def __init__(self):
        super.__init__()
        self.fly = False

    def drive(self):
        return "car is driving"





from transport_class import Transport

class Plane(Transport):
    def __init__(self):
        super.__init__()
        self.fly = True

    def fly(self):
        return "plane is flying"


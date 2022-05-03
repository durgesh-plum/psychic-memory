from transport_class import Transport

class Boat(Transport):
    def __init__(self):
        super.__init__()
        self.float = True

    def sail(self):
        return "boat is sailing"

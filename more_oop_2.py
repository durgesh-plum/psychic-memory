from more_oop import A

class B(A):
    def __init__(self):
        super().__init__()
        self.class_attribute = "This is class B"

    def class_b_method(self):
        return "This is class B method"

print("Running more OOP_2" + __name__)

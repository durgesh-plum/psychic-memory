class Dog:

    animal_kind = 'canine' #class variable

    def __init__(self,name):
        self.name = name
        self.animal_kind = "canine"

    def bark(self): #method
        print(self.animal_kind)
        return "Woof!"

bob = Dog()
luna = Dog()

bob.animal_kind = "Big Dog"


print(bob.animal_kind)
print(luna.animal_kind)




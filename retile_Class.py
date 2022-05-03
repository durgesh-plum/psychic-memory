from animal_class import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True

    def use_venom(self):
        return "using venom"




snake = Reptile()
print(snake.breathe())
print(snake.alive)
print(snake.use_venom())
snake.set_location("forrest")
print(snake.get_location())

cat = Animal()

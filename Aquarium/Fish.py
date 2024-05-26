import Animal

MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8


class Fish(Animal.Animal):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH)
        self.width = MAX_FISH_WIDTH
        self.height = MAX_FISH_HEIGHT
        self.directionV = directionV  # random 0 - down / 1 - up

    def __str__(self):
        st = "The fish " + str(self.name) + " is " + str(self.age) + " years old and has " + str(self.food) + " food"
        return st

    def up(self):
        self.y = self.y - 1

    def down(self):
        self.y = self.y + 1

    def starvation(self):
        super(Fish, self).starvation()

    def die(self):
        super(Fish, self).die()

    def get_directionV(self):
        return self.directionV

    def set_directionV(self, directionV):
        self.directionV = directionV


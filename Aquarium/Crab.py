import Animal

MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7


class Crab(Animal.Animal):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name,age,x, y,directionH)
        self.width = MAX_CRAB_WIDTH
        self.height = MAX_CRAB_HEIGHT


    def __str__(self):
        st = "The crab " + str(self.name) + " is " + str(self.age) + " years old and has " + str(self.food) + " food"
        return st

    def starvation(self):
        super(Crab, self).starvation()
        pass

    def die(self):
        super(Crab, self).die()

import Crab


class Shrimp(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.height = 3
        self.width = 7
        self.y = y - self.height-1


    def get_animal(self):
        if self.directionH == 0:
            shrimp = [["*", " ", " "], [" ", "*", " "], ["*", "*", "*"], [" ", "*", " "], [" ", "*", "*"], [" ", "*", " "], [" ", "*", " "]]
        else:
            shrimp = [[" ", "*", " "], [" ", "*", " "], [" ", "*", "*"], [" ", "*", " "], ["*", "*", "*"], [" ", "*", " "], ["*", " ", " "]]
        return shrimp

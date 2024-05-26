import Crab


class Ocypode(Crab.Crab):
    def __init__(self, name, age, x, y , directionH):
        super().__init__(name,age,x, y,directionH)
        self.width = 7
        self.height = 4
        self.y = y - self.height-1


    def get_animal(self):
        crab = [[" ", " ", "*", "*"], ["*", " ", "*", " "], [" ", "*", "*", " "], [" ", "*", "*", " "], [" ", "*", "*", " "], ["*", " ", "*", " "], [" ", " ", "*", "*"]]
        return crab

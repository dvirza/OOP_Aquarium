MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
STARTING_FOOD = 5
MAX_AGE = 120


class Animal:
    def __init__(self, name, age, x, y, directionH):
        self.alive = True
        self.width = MAX_ANIMAL_HEIGHT
        self.height = MAX_ANIMAL_HEIGHT
        self.food = STARTING_FOOD
        self.name = name
        self.age = age
        self.x = x
        self.y = y
        self.directionH = directionH  # random 0 - left / 1 - right

    def __str__(self):
        super(Animal, self).__str__()
        pass

    def get_food(self):
        return self.food
        pass

    def get_age(self):
        return self.age
        pass

    def dec_food(self):
        self.food = self.food - 1


    def inc_age(self):
        self.age = self.age + 1


    def right(self):
        self.x = self.x + 1

    def left(self):
        self.x = self.x - 1

    def get_position(self):
        return self.x, self.y
        pass

    def set_x(self, x):
        self.x = x
        pass

    def set_y(self, y):
        self.y = y

    def starvation(self):
        if self.food == 0:
           self.alive = False

    def die(self):
        self.alive = False


        pass

    def get_directionH(self):
        return self.directionH
        pass



    def set_directionH(self, directionH):
        self.directionH = directionH

    def get_alive(self):
        return self.alive


    def get_size(self):
        return self.getWidth(), self.getWidth()


    def get_food_amount(self):
        return self.food


    def add_food(self, amount):
        self.food += amount


    def get_animal(self):
        pass

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

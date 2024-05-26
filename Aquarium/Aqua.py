import Animal
import Fish
import Crab
import Shrimp
import Scalar
import Moly
import Ocypode

MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7
MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8
WATERLINE = 3
FEED_AMOUNT = 10
MAX_AGE = 120
turn = 0

class Aqua:
    def __init__(self, aqua_width, aqua_height):
        self.turn = 0
        self.aqua_height = aqua_height
        self.aqua_width = aqua_width
        self.board = [' '] * self.aqua_height #colum *1
        self.build_tank()
        self.anim = []

    def build_tank(self):
        temp = []
        for i in range(self.aqua_width):
            temp.append(self.board.copy())

        self.board = temp
        for y in range(self.aqua_height): #builds aquarium
            for x in range(self.aqua_width):
                if (x == 0 or x == self.aqua_width -1) and (y != self.aqua_height-1):
                    self.board[x][y] = "|"
                elif y == 1 and x != 0 and x != self.aqua_width-1:
                    self.board[x][y] = '~'
                elif y == self.aqua_height-1:
                    self.board[x][y] = '_'
        self.board[0][self.aqua_height-1] = '\\'
        self.board[self.aqua_width-1][self.aqua_height-1] = '/'


        self.print_board()

    def print_board(self):
        for i in range(self.aqua_height):
            for j in range(self.aqua_width):
               print(self.board[j][i],end= '')
            print("\n",end= "")
        pass

    def get_board(self):
        return self.board


    def get_all_animal(self):
        """
        Returns the array that contains all the animals
        """
        return self.anim


    def is_collision(self, animal):
        """
        Returns True if the next step of the crab is a collision
        """
        if isinstance(animal,Crab.Crab):

            for anim in self.anim:
                if isinstance(anim,Crab.Crab):
                    if animal.directionH == 0:
                        if -1 < animal.x - (anim.x + anim.width) <  2 :
                            return True
                    if animal.directionH == 1:
                        if -1 < anim.x - (animal.x + animal.width) < 2 :
                            return True
        return False



    def print_animal_on_board(self, animal: Animal):
        if animal.y+animal.height >= self.aqua_height:
            self.anim.remove(animal)
            return
        if animal.x+animal.width >= self.aqua_width:
            self.anim.remove(animal)
            return

        for i in range(animal.height):
            for j in range(animal.width):
                self.board[animal.x+j][animal.y+i] = animal.get_animal()[j][i]


    def delete_animal_from_board(self, animal: Animal):
        for i in range(animal.height):
            for j in range(animal.width):
                self.board[animal.x + j][animal.y + i] = ' '
        pass

    def add_fish(self, name, age, x, y, directionH, directionV, fishtype):
        """
        Adding fish to the aquarium
        """
        if fishtype == 'sc':
            newfish = Scalar.Scalar(name,age,x,y,directionH,directionV)
            if not self.checkSize(x,y,newfish.getWidth()-1,newfish.getHeight()-1):
                return False
            if y + newfish.getHeight() > self.aqua_height - MAX_CRAB_HEIGHT:
                print('The Fish cant cross the crabs line')
                return False
            self.anim.append(newfish)


        if fishtype == 'mo':
            newfish = Moly.Moly(name,age,x,y,directionH,directionV)
            if not self.checkSize(x,y,newfish.getWidth(),newfish.getHeight()):
                return False
            self.anim.append(newfish)
        self.print_animal_on_board(newfish)
        return True
    def checkSize(self,x,y,ranX,ranY):
        for i in range(ranX):
            for j in range(ranY):
                if not self.check_if_free(x + i, y + j):
                    return False

        return True

    def add_crab(self, name, age, x, y, directionH, crabtype):
        """
        Adding crab to the aquarium
        """
        if crabtype == 'oc':
            newcrab = Ocypode.Ocypode(name,age,x,y, directionH)
            if not self.checkSize(x, y-newcrab.getHeight(), newcrab.getWidth(), newcrab.getHeight()):
                return False
            self.anim.append(newcrab)
        if crabtype == 'sh':
            newcrab = Shrimp.Shrimp(name, age,x,y, directionH)
            if not self.checkSize(x, y-newcrab.getHeight(), newcrab.getWidth(), newcrab.getHeight()):
                return False
            self.anim.append(newcrab)
        self.print_animal_on_board(newcrab)
        return True


    def check_if_free(self, x, y) -> bool:
        """
        method for checking whether the position is empty before inserting a new animal
        """
        for animal in self.anim:
            if animal.x <= x < animal.width+animal.x and animal.y <= y < animal.height + animal.y:
                print(x,",",y)
                return False

        return True


    def left(self, a):
        self.delete_animal_from_board(a)
        a.left()
        self.print_animal_on_board(a)


    def right(self, a):
        self.delete_animal_from_board(a)
        a.right()
        self.print_animal_on_board(a)

    def up(self, a):
        self.delete_animal_from_board(a)
        a.up()
        self.print_animal_on_board(a)
        pass

    def down(self, a):
        self.delete_animal_from_board(a)
        a.down()
        self.print_animal_on_board(a)
        pass

    def will_hit(self,animal: Animal):
        if animal.directionH == 1:
            if self.board[animal.x + animal.getWidth() + 1][animal.y] == '|':
                return 1
        if animal.directionH == 0:
            if self.board[animal.x - 1][animal.y] == '|':
                return 2
        if isinstance(animal,Fish.Fish):
            if animal.directionV == 1:
                if self.board[animal.x][animal.y - 1] == '~':
                    return 3
            if animal.directionV == 0:
                if self.board[animal.x][animal.y + animal.getHeight() + MAX_CRAB_HEIGHT] == '_':
                    return 4


    def next_turn(self):
        """
        Managing a single step
        """

        if self.turn % 10 == 0:
            for anim in self.anim:
                anim.dec_food()
                if anim.food == 0:
                    anim.starvation()
                if self.turn % 100 == 0:
                    anim.inc_age()
            for anim in self.anim:
                if not anim.get_alive():
                    self.delete_animal_from_board(anim)
                    self.anim.remove(anim)


        collided = []
        for anim in self.anim:
            if self.is_collision(anim):
                collided.append(anim)

        for c in collided:
            if c.directionH == 0:
                Animal.Animal.set_directionH(c,1)
            else:
                Animal.Animal.set_directionH(c,0)



        for anim in self.anim:
            if self.will_hit(anim) == 1:
                Animal.Animal.set_directionH(anim,0)
            if self.will_hit(anim) == 2:
                Animal.Animal.set_directionH(anim,1)
            if self.will_hit(anim) == 3:
                Fish.Fish.set_directionV(anim,0)
            if self.will_hit(anim) == 4:
                Fish.Fish.set_directionV(anim,1)

        for anim in self.anim:
            if anim not in collided:
                if anim.directionH == 0:
                    self.left(anim)
                if anim.directionH == 1:
                    self.right(anim)
            else:
                self.delete_animal_from_board(anim)
                self.print_animal_on_board(anim)
            if isinstance(anim,Fish.Fish):
                if anim.directionV == 1:
                    self.up(anim)
                if anim.directionV == 0:
                    self.down(anim)

        self.turn += 1



    def print_all(self):
        """
        Prints all the animals in the aquarium
        """
        self.get_all_animal()
        for anim in self.anim:
            print(anim)
        pass

    def feed_all(self):
        """
        feed all the animals in the aquarium
        """
        for anim in self.anim:
            Animal.Animal.add_food(anim,10)


    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        if animaltype == 'sc' or animaltype == 'mo':
            return self.add_fish(name, age, x, y, directionH, directionV, animaltype)
        elif animaltype == 'oc' or animaltype == 'sh':
            return self.add_crab(name, age, x, self.aqua_height , directionH, animaltype)
        else:
            return False

    def several_steps(self) -> None:
        """
        Managing several steps
        """
        n = int(input("How many steps you want to take forward? "))
        for i in range(n):
            self.next_turn()

        pass



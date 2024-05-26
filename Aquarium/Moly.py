import Fish


class Moly(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name,age,x,y,directionH,directionV)
        self.height = 3
        self.width = 7

    def get_animal(self):
        if self.directionH == 1:
            moly = [['*','*','*'],[' ','*',' '],[' ','*',' '],['*','*','*'],['*','*','*'],['*','*','*'],[' ','*',' ']]
        else:
            moly = [[' ','*',' '],['*','*','*'],['*','*','*'],['*','*','*'],[' ','*',' '],[' ','*',' '],['*','*','*']]
        return moly
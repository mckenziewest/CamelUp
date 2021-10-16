import random
#defining camels
class Camel:
    #attributes
    def __init__(self, color = None, above = None, below = None, space = 0):
        self.color = color
        self.above = above
        self.below = below
        self.space = space
    
    #functions
    def get_color(self)
        return self.color
    
    
    def get_above(self):
        return self.above
    
    
    def get_below(self):
        return self.above()
   
    
    def new_above(self,newabove):
        self.above = newabove
    
    
    def new_below(self,newbelow):
        self.below = newbelow
    
    
    def roll(self):
        die = random.randint(1,3)
        if self.color == "Black" or self.color == 'White':
            self.space -= die
        else:
            self.space += die

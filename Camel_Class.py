import random
#defining camels
class Camel:
    colors = ["Red",'Blue',"Green","Yellow","Purple","Orange", "White", "Black"]
    c = colors.pop(random.randint(0,len(colors)-1))
    s = 0
    a = colors.pop(random.randint(0,len(colors)-1))
    b = colors.pop(random.randint(0,len(colors)-1))
    #attributes
    def __init__(self, color = c, space = s, above = a, below = b):
        self.color = color
        self.space = space
        self.above = above
        self.below = below
    def get_color(self):
        return self.color       
    def roll(self):
        die = random.randint(1,3)
        if self.color == "Black" or self.color == 'White':
            self.space -= die
        else:
            self.space += die
        print(self.space)
camel = Camel()
camel.get_color()
camel.roll()
camel.change_space()
#Need to figure out how to get this to interact with other camels for movement
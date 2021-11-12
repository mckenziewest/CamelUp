
import random

import pandas

def Output_Board(Round):
    x = [" _______  _______  _______  _______  _______  _______  _______  _______  _______  _______  _______  _______  _______  _______  _______  _______",
         "    1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       16  "]
    for i in range(0,2):
        print(x[i])
    if Round == 0:
        print("\n                                                                     SET UP")
    else:
        print("\n                                                                  END OF ROUND #{} \n".format(Round))

def Print_Red():
    x = ["         ","   RED   "]
    return x
def Print_Blue():
    x = ["         ","  BLUE   "]
    return x
def Print_Green():
    x = ["         ","  GREEN  "]
    return x
def Print_Purple():
    x = ["         ","  PURPLE "]
    return x
def Print_Yellow():
    x = ["         ","  YELLOW "]
    return x
def Print_Black():
    x = ["         ","  BLACK  "]
    return x
def Print_White():
    x = ["         ","  WHITE  "]
    return x
def Empty_Space():
    x = ["         ","         "]
    return x



class Camel:

    def __init__(self, color):
        self.color = color
        if (color == "BLACK") or (color == "WHITE"):
            self.position = 17
        else:
            self.position = 0 #0 is pre-first round, then 1-16 after
        self.height = 1 #1 is only one camel up, 2 is a camel stacked on another
        self.camel_above = None
        self.camel_below = None

    def Change_Position(self, Number):
        self.position += Number #changed from =

    def Change_Height(self, Height):
        self.height = Height

    def Change_Camel_Above(self, Camel):
        self.camel_above = Camel

    def Change_Camel_Below(self, Camel):
        self.camel_below = Camel

    def Change_Position_B_or_W(self, Number):
        self.position -= Number #subtracting whatever was roled


def PLAY_GAME():
    Color_List = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE"]
    Color_Dict = {
        "RED":red, "BLUE":blue, "GREEN":green, "PURPLE":purple, "YELLOW":yellow, "BLACK":black, "WHITE":white
    }
    First_Dict = {                                                                        #Dict to reconize if spaces are taken
        1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False,
        9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False
    }
    Second_Dict = {                                                           #Dict for heights on each space
        1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0,
        9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0
    }

    for i in range(0,5): #set up
        Appended_Color = random.choice(Color_List) #picks color from Color_List
        Color_List.remove(Appended_Color)
        Rolled_Number = random.randint(1,3) #1,2,3
        Picked_Color = Color_Dict[Appended_Color]

        if (red.position == Rolled_Number) and (red.camel_above == None): #check occupied space, check if camel is above
            red.Change_Camel_Above(Appended_Color) #changing None to string color
            Picked_Color.Change_Camel_Below("RED")
            Picked_Color.Change_Height(red.height + 1)
            Picked_Color.Change_Position(Rolled_Number)
            First_Dict[Rolled_Number] = True
            Second_Dict[Rolled_Number] = Picked_Color.height

        elif (blue.position == Rolled_Number) and (blue.camel_above == None):
            blue.Change_Camel_Above(Appended_Color)
            Picked_Color.Change_Camel_Below("BLUE")
            Picked_Color.Change_Height(blue.height + 1)
            Picked_Color.Change_Position(Rolled_Number)
            First_Dict[Rolled_Number] = True
            Second_Dict[Rolled_Number] = Picked_Color.height

        elif (green.position == Rolled_Number) and (green.camel_above == None):
            green.Change_Camel_Above(Appended_Color)
            Picked_Color.Change_Camel_Below("GREEN")
            Picked_Color.Change_Height(green.height + 1)
            Picked_Color.Change_Position(Rolled_Number)
            First_Dict[Rolled_Number] = True
            Second_Dict[Rolled_Number] = Picked_Color.height

        elif (yellow.position == Rolled_Number) and (yellow.camel_above == None):
            yellow.Change_Camel_Above(Appended_Color)
            Picked_Color.Change_Camel_Below("YELLOW")
            Picked_Color.Change_Height(yellow.height + 1)
            Picked_Color.Change_Position(Rolled_Number)
            First_Dict[Rolled_Number] = True
            Second_Dict[Rolled_Number] = Picked_Color.height

        elif (purple.position == Rolled_Number) and (purple.camel_above == None):
            purple.Change_Camel_Above(Appended_Color)
            Picked_Color.Change_Camel_Below("PURPLE")
            Picked_Color.Change_Height(purple.height + 1)
            Picked_Color.Change_Position(Rolled_Number)
            First_Dict[Rolled_Number] = True
            Second_Dict[Rolled_Number] = Picked_Color.height

        else:
            Picked_Color.Change_Position(Rolled_Number)
            First_Dict[Rolled_Number] = True
            Second_Dict[Rolled_Number] = Picked_Color.height

    B_W_List = ["BLACK", "WHITE"]
    for i in range(0,2):
        Appended_Color = random.choice(B_W_List) #picks color from Color_List
        B_W_List.remove(Appended_Color)
        Rolled_Number = random.randint(1,3) #1,2,3
        Picked_Color = Color_Dict[Appended_Color]

        if (black.position == 17 - Rolled_Number) and (black.camel_above == None):
            black.Change_Camel_Above(Appended_Color)
            Picked_Color.Change_Camel_Below("BLACK")
            Picked_Color.Change_Height(black.height + 1)
            Picked_Color.Change_Position_B_or_W(Rolled_Number)
            First_Dict[17 - Rolled_Number] = True
            Second_Dict[17 - Rolled_Number] = Picked_Color.height

        elif (white.position == 17 - Rolled_Number) and (white.camel_above == None):
            white.Change_Camel_Above(Appended_Color)
            Picked_Color.Change_Camel_Below("WHITE")
            Picked_Color.Change_Height(white.height + 1)
            Picked_Color.Change_Position_B_or_W(Rolled_Number)
            First_Dict[Rolled_Number] = True
            Second_Dict[Rolled_Number] = Picked_Color.height

        else:
            Picked_Color.Change_Position_B_or_W(Rolled_Number)
            First_Dict[17 - Rolled_Number] = True
            Second_Dict[17 - Rolled_Number] = Picked_Color.height

    Color_Def_Dict = {
        "RED":Print_Red(), "BLUE":Print_Blue(), "GREEN":Print_Green(), "PURPLE":Print_Purple(),
        "YELLOW":Print_Yellow(), "BLACK":Print_Black(), "WHITE":Print_White()
    }
    Color_List = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "WHITE"]
    Adding_To_List = []
    for i in range(5,0, -1): #5,4,3,2,1 heights
        for j in range(1,17): #1 - 16 spaces
            counter = 0
            for k in range(0,len(Color_List)):
                if (Color_Dict[Color_List[k]].position == j) and (Color_Dict[Color_List[k]].height == i):
                    Adding_To_List.append(Color_Def_Dict[Color_List[k]])
                    counter += 1
            if counter == 0:
                Adding_To_List.append(Empty_Space())

    Current_Round = 0

    for w in range(1,6): #1,2,3,4,5 height
        New_List = []
        for p in range(0,2): #length of cells
            New_List.append(Adding_To_List[(16*w)-16][p]+Adding_To_List[(16*w)-15][p]+Adding_To_List[(16*w)-14][p]+Adding_To_List[(16*w)-13][p]+Adding_To_List[(16*w)-12][p]+Adding_To_List[(16*w)-11][p]+Adding_To_List[(16*w)-10][p]+Adding_To_List[(16*w)-9][p]+Adding_To_List[(16*w)-8][p]+Adding_To_List[(16*w)-7][p]+Adding_To_List[(16*w)-6][p]+Adding_To_List[(16*w)-5][p]+Adding_To_List[(16*w)-4][p]+Adding_To_List[(16*w)-3][p]+Adding_To_List[(16*w)-2][p]+Adding_To_List[(16*w)-1][p])
        for u in range(0,2):
            print(New_List[u])

    Output_Board(Current_Round) #function

    # ^^^ All above is to print the board game, below is to play game





    Number_Of_Rounds = int(input("How many rounds should we play: "))
    for i in range(0,Number_Of_Rounds): #number of rounds played        COUNTS EACH ROUND
        Dice_List = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "B/W"]
        for j in range(0,5): #number of dice rolled                     COUNTS EACH DICE ROLE
            Dice = random.choice(Dice_List) #string                     DICE COLOR
            Dice_List.remove(Dice)
            Number = random.randint(1,3) #1,2,3                  NUMBER ON DICE

            #print("\nRound Number: {:<5} Color Moved: {:<8}   Dice Number Rolled:  {:<5}   Roles Left: {:<5}".format(i,Dice, Number, 5-(j+1)))         USED TO CHECK
            #print(First_Dict)                                                                                                                          USED TO CHECK
            #print(Second_Dict)                                                                                                                         USED TO CHECK

            if Dice != "B/W":
                Color = Color_Dict[Dice]
                Original_Camel_Position = Color.position
                Color.Change_Position(Number) #new position

                if First_Dict[Color.position] == False:                 #no camels are in the new occupried spot
                    if Color.height == 1:                               #not changing heights
                        First_Dict[Original_Camel_Position] = False     #change old position of stack to empty
                        First_Dict[Color.position] = True               #change new position to occupied
                        Second_Dict[Color.position] = Second_Dict[Original_Camel_Position]
                        Second_Dict[Original_Camel_Position] = 0

                        while Color.camel_above != None:
                            New_Camel_Color = Color_Dict[Color.camel_above]
                            Color = New_Camel_Color
                            Color.Change_Position(Number)

                        #Case (2)

                    else: #no camels and moving down spaces

                        Bottom_Of_Choice = Color_Dict[Color.camel_below]
                        Bottom_Of_Choice.Change_Camel_Above(None)
                        Color.Change_Camel_Below(None)

                        Second_Dict[Color.position] = Second_Dict[Original_Camel_Position]-(Color.height - 1)       #subtract total stack from OG height -1 for new height on space
                        Second_Dict[Original_Camel_Position] = Color.height - 1                                     #change OG spot height to picked color -1
                        First_Dict[Color.position] = True                                                           #change new position to occupied as no camel there
                        Height_Change_Of_Camel = Color.height -1                                                    #how much each camel is going to be moved down

                        while Color.camel_above != None:
                            Color.Change_Height(Color.height - Height_Change_Of_Camel)
                            New_Camel_Color = Color_Dict[Color.camel_above]
                            Color = New_Camel_Color
                            Color.Change_Position(Number)

                        if Color.camel_above == None:
                            Color.Change_Height(Color.height - Height_Change_Of_Camel)

                        #Case (4)

                else: #a camel is in our new spot
                    if Color.height - 1 == Second_Dict[Color.position]: #height stays the same

                        Bottom_Of_Choice = Color_Dict[Color.camel_below]                    #adjusting camel above to None
                        Bottom_Of_Choice.Change_Camel_Above(None)

                        Dice_List_2 = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "WHITE"]          #four lines below change "new color"'s below camel
                        for q in range(0,len(Dice_List_2)): #0,5
                            if (Color_Dict[Dice_List_2[q]].position == Color.position) and (Color_Dict[Dice_List_2[q]].camel_above == None) and (Color.color != Dice_List_2[q]): #find top of new stack
                                Color.Change_Camel_Below(Dice_List_2[q]) #changed from
                                Other_Color = Color_Dict[Dice_List_2[q]]
                                Other_Color.Change_Camel_Above(Color.color)

                        Count_Of_Camels = 1                 #count to add to total heights

                        while Color.camel_above != None:
                            New_Camel_Color = Color_Dict[Color.camel_above]
                            Color = New_Camel_Color
                            Color.Change_Position(Number)
                            Count_Of_Camels += 1

                        Second_Dict[Original_Camel_Position] -= Count_Of_Camels #redcues OG spot by number of camels moved
                        Second_Dict[Color.position] += Count_Of_Camels

                        #Case (5)

                    elif Color.height - 1 <= Second_Dict[Color.position]: #height needs to increase

                        if Color.camel_below == None:
                            Height_Of_New_Stack = Second_Dict[Color.position]
                            First_Dict[Original_Camel_Position] = False
                            Second_Dict[Color.position] += Second_Dict[Original_Camel_Position]
                            Second_Dict[Original_Camel_Position] = 0

                            Dice_List_2 = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "WHITE"]              #next 6 lines cover camel_below and camel_above
                            for q in range(0,len(Dice_List_2)): #0,1,2,3,4
                                if (Color_Dict[Dice_List_2[q]].position == Color.position) and (Color_Dict[Dice_List_2[q]].camel_above == None) and (Color.color != Dice_List_2[q]): #find top of new stack
                                    Color.Change_Camel_Below(Dice_List_2[q])
                                    Other_Color = Color_Dict[Dice_List_2[q]]
                                    Other_Color.Change_Camel_Above(Color.color)

                                    while Color.camel_above != None:
                                        Color.Change_Height(Color.height + Height_Of_New_Stack)
                                        New_Camel_Color = Color_Dict[Color.camel_above]
                                        Color = New_Camel_Color
                                        Color.Change_Position(Number)

                                    if Color.camel_above == None:
                                        Color.Change_Height(Color.height + Height_Of_New_Stack)

                            #Case (1.1)

                        else:
                            Change_In_Height = Second_Dict[Color.position] - Color.height + 1
                            Second_Dict[Color.position] += Second_Dict[Original_Camel_Position] - Color_Dict[Color.camel_below].height          #new space change second dict
                            Second_Dict[Original_Camel_Position] = Color_Dict[Color.camel_below].height                    #Camel being left change second dict
                            Color_Dict[Color.camel_below].Change_Camel_Above(None)

                            Dice_List_2 = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "WHITE"]              #next 6 lines cover camel_below and camel_above
                            for q in range(0,len(Dice_List_2)):
                                if (Color_Dict[Dice_List_2[q]].position == Color.position) and (Color_Dict[Dice_List_2[q]].camel_above == None) and (Color.color != Dice_List_2[q]): #find top of new stack
                                    Color.Change_Camel_Below(Dice_List_2[q])
                                    Other_Color = Color_Dict[Dice_List_2[q]]
                                    Other_Color.Change_Camel_Above(Color.color)

                                    while Color.camel_above != None:
                                        Color.Change_Height(Color.height + Change_In_Height)
                                        New_Camel_Color = Color_Dict[Color.camel_above]
                                        Color = New_Camel_Color
                                        Color.Change_Position(Number)

                                    if Color.camel_above == None:
                                        Color.Change_Height(Color.height + Change_In_Height)

                            #Case (1.2)

                        #Case (1)

                    else: #height going down onto a camel
                        Change_In_Height = Second_Dict[Original_Camel_Position] - Second_Dict[Color.position] - 1   #subtract from current height
                        Color_Dict[Color.camel_below].Change_Camel_Above(None)
                        Second_Dict[Color.position] += Second_Dict[Original_Camel_Position] - Color_Dict[Color.camel_below].height #CHECK
                        Second_Dict[Original_Camel_Position] = Color_Dict[Color.camel_below].height

                        Dice_List_2 = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "WHITE"]              #next 6 lines cover camel_below and camel_above
                        for q in range(0,len(Dice_List_2)): #0,1,2,3,4
                            if (Color_Dict[Dice_List_2[q]].position == Color.position) and (Color_Dict[Dice_List_2[q]].camel_above == None) and (Color.color != Dice_List_2[q]): #find top of new stack
                                Color.Change_Camel_Below(Dice_List_2[q])
                                Other_Color = Color_Dict[Dice_List_2[q]]
                                Other_Color.Change_Camel_Above(Color.color)


                                while Color.camel_above != None:
                                    Color.Change_Height(Color.height - Change_In_Height)
                                    New_Camel_Color = Color_Dict[Color.camel_above]
                                    Color = New_Camel_Color
                                    Color.Change_Position(Number)

                                if Color.camel_above == None:
                                    Color.Change_Height(Color.height - Change_In_Height)

                        #Case (3)

            else: #Black or White case
                Dice = random.choice(['WHITE', 'BLACK'])
                Color = Color_Dict[Dice]                    #Now we have Color and Number roled
                Original_Camel_Position = Color.position
                Color.Change_Position_B_or_W(Number)        #new position

                if First_Dict[Color.position] == False:                 #no camels are in the new occupried spot
                    if Color.height == 1:                               #not changing heights
                        First_Dict[Original_Camel_Position] = False     #change old position of stack to empty
                        First_Dict[Color.position] = True               #change new position to occupied
                        Second_Dict[Color.position] = Second_Dict[Original_Camel_Position]
                        Second_Dict[Original_Camel_Position] = 0

                        while Color.camel_above != None:
                            New_Camel_Color = Color_Dict[Color.camel_above]
                            Color = New_Camel_Color
                            Color.Change_Position_B_or_W(Number)

                        #Case (7)

                    else: #no camels and moving down spaces

                        Bottom_Of_Choice = Color_Dict[Color.camel_below]
                        Bottom_Of_Choice.Change_Camel_Above(None)
                        Color.Change_Camel_Below(None)

                        Second_Dict[Color.position] = Second_Dict[Original_Camel_Position]-(Color.height - 1)       #subtract total stack from OG height -1 for new height on space
                        Second_Dict[Original_Camel_Position] = Color.height - 1                                     #change OG spot height to picked color -1
                        First_Dict[Color.position] = True                                                           #change new position to occupied as no camel there
                        Height_Change_Of_Camel = Color.height -1                                                    #how much each camel is going to be moved down

                        while Color.camel_above != None:
                            Color.Change_Height(Color.height - Height_Change_Of_Camel)
                            New_Camel_Color = Color_Dict[Color.camel_above]
                            Color = New_Camel_Color
                            Color.Change_Position_B_or_W(Number)

                        if Color.camel_above == None:
                            Color.Change_Height(Color.height - Height_Change_Of_Camel)

                        #Case (9)

                else: #a camel is in our new spot
                    if Color.height - 1 == Second_Dict[Color.position]: #height stays the same

                        Bottom_Of_Choice = Color_Dict[Color.camel_below]                    #adjusting camel above to None
                        Bottom_Of_Choice.Change_Camel_Above(None)

                        Dice_List_2 = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "WHITE"]          #four lines below change "new color"'s below camel
                        for q in range(0,len(Dice_List_2)): #0,6
                            if (Color_Dict[Dice_List_2[q]].position == Color.position) and (Color_Dict[Dice_List_2[q]].camel_above == None) and (Color.color != Dice_List_2[q]): #find top of new stack
                                Color.Change_Camel_Below(Dice_List_2[q]) #changed from
                                Other_Color = Color_Dict[Dice_List_2[q]]
                                Other_Color.Change_Camel_Above(Color.color)

                        Count_Of_Camels = 1                 #count to add to total heights

                        while Color.camel_above != None:
                            New_Camel_Color = Color_Dict[Color.camel_above]
                            Color = New_Camel_Color
                            Color.Change_Position_B_or_W(Number)
                            Count_Of_Camels += 1

                        Second_Dict[Original_Camel_Position] -= Count_Of_Camels #redcues OG spot by number of camels moved
                        Second_Dict[Color.position] += Count_Of_Camels

                        #Case (10)

                    elif Color.height - 1 <= Second_Dict[Color.position]: #height needs to increase

                        if Color.camel_below == None:
                            Height_Of_New_Stack = Second_Dict[Color.position]
                            First_Dict[Original_Camel_Position] = False
                            Second_Dict[Color.position] += Second_Dict[Original_Camel_Position]
                            Second_Dict[Original_Camel_Position] = 0

                            Dice_List_2 = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "WHITE"]              #next 6 lines cover camel_below and camel_above
                            for q in range(0,len(Dice_List_2)): #0,1,2,3,4
                                if (Color_Dict[Dice_List_2[q]].position == Color.position) and (Color_Dict[Dice_List_2[q]].camel_above == None) and (Color.color != Dice_List_2[q]): #find top of new stack
                                    Color.Change_Camel_Below(Dice_List_2[q])
                                    Other_Color = Color_Dict[Dice_List_2[q]]
                                    Other_Color.Change_Camel_Above(Color.color)

                                    while Color.camel_above != None:
                                        Color.Change_Height(Color.height + Height_Of_New_Stack)
                                        New_Camel_Color = Color_Dict[Color.camel_above]
                                        Color = New_Camel_Color
                                        Color.Change_Position_B_or_W(Number)

                                    if Color.camel_above == None:
                                        Color.Change_Height(Color.height + Height_Of_New_Stack)

                            #Case (6.1)

                        else:
                            Change_In_Height = Second_Dict[Color.position] - Color.height + 1
                            Second_Dict[Color.position] += Second_Dict[Original_Camel_Position] - Color_Dict[Color.camel_below].height          #new space change second dict
                            Second_Dict[Original_Camel_Position] = Color_Dict[Color.camel_below].height                    #Camel being left change second dict
                            Color_Dict[Color.camel_below].Change_Camel_Above(None)

                            Dice_List_2 = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "WHITE"]              #next 6 lines cover camel_below and camel_above
                            for q in range(0,len(Dice_List_2)):
                                if (Color_Dict[Dice_List_2[q]].position == Color.position) and (Color_Dict[Dice_List_2[q]].camel_above == None) and (Color.color != Dice_List_2[q]): #find top of new stack
                                    Color.Change_Camel_Below(Dice_List_2[q])
                                    Other_Color = Color_Dict[Dice_List_2[q]]
                                    Other_Color.Change_Camel_Above(Color.color)

                                    while Color.camel_above != None:
                                        Color.Change_Height(Color.height + Change_In_Height)
                                        New_Camel_Color = Color_Dict[Color.camel_above]
                                        Color = New_Camel_Color
                                        Color.Change_Position_B_or_W(Number)

                                    if Color.camel_above == None:
                                        Color.Change_Height(Color.height + Change_In_Height)

                            #Case (6.2)

                        #Case (6)

                    else: #height going down onto a camel
                        Change_In_Height = Second_Dict[Original_Camel_Position] - Second_Dict[Color.position] - 1   #subtract from current height
                        Color_Dict[Color.camel_below].Change_Camel_Above(None)
                        Second_Dict[Color.position] += Second_Dict[Original_Camel_Position] - Color_Dict[Color.camel_below].height #CHECK
                        Second_Dict[Original_Camel_Position] = Color_Dict[Color.camel_below].height

                        Dice_List_2 = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "WHITE"]              #next 6 lines cover camel_below and camel_above
                        for q in range(0,len(Dice_List_2)): #0,1,2,3,4
                            if (Color_Dict[Dice_List_2[q]].position == Color.position) and (Color_Dict[Dice_List_2[q]].camel_above == None) and (Color.color != Dice_List_2[q]): #find top of new stack
                                Color.Change_Camel_Below(Dice_List_2[q])
                                Other_Color = Color_Dict[Dice_List_2[q]]
                                Other_Color.Change_Camel_Above(Color.color)

                                while Color.camel_above != None:
                                    Color.Change_Height(Color.height - Change_In_Height)
                                    New_Camel_Color = Color_Dict[Color.camel_above]
                                    Color = New_Camel_Color
                                    Color.Change_Position_B_or_W(Number)

                                if Color.camel_above == None:
                                    Color.Change_Height(Color.height - Change_In_Height)

                        #Case (8)


            #v = [[red.color, red.position, red.height, red.camel_above, red.camel_below],                          #USED TO CHECK
            #blue.color, blue.position, blue.height, blue.camel_above, blue.camel_below],                           #USED TO CHECK
            #[green.color, green.position, green.height, green.camel_above, green.camel_below],                     #USED TO CHECK
            #[yellow.color,yellow.position, yellow.height, yellow.camel_above, yellow.camel_below],                 #USED TO CHECK
            #[purple.color, purple.position, purple.height, purple.camel_above, purple.camel_below],                #USED TO CHECK
            #[black.color,black.position, black.height, black.camel_above, black.camel_below],                      #USED TO CHECK
            #[white.color, white.position, white.height, white.camel_above, white.camel_below] ]                    #USED TO CHECK
            #print("\n{:<8} {:<15} {:<10} {:<10} {:<10}".format('Color','Position','Height','C_Above','C_Below'))   #USED TO CHECK
            #for d in range(0,7):                                                                                   #USED TO CHECK
                #print("{:<8} {:<15} {:<10} {:<10} {:<10}".format(v[d][0], v[d][1], v[d][2], v[d][3], v[d][4]))     #USED TO CHECK

        Current_Round += 1



    #below is printing the simulation after so many rounds

    Color_List = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "WHITE"]
    Adding_To_List = []
    for i in range(5,0, -1): #5,4,3,2,1 heights
        for j in range(1,17): #1 - 16 spaces
            counter = 0
            for k in range(0,len(Color_List)):
                if (Color_Dict[Color_List[k]].position == j) and (Color_Dict[Color_List[k]].height == i):
                    Adding_To_List.append(Color_Def_Dict[Color_List[k]])
                    counter += 1
            if counter == 0:
                Adding_To_List.append(Empty_Space())

    for w in range(1,6): #1,2,3,4,5 height
        New_List = []
        for p in range(0,2): #length of cells
            New_List.append(Adding_To_List[(16*w)-16][p]+Adding_To_List[(16*w)-15][p]+Adding_To_List[(16*w)-14][p]+Adding_To_List[(16*w)-13][p]+Adding_To_List[(16*w)-12][p]+Adding_To_List[(16*w)-11][p]+Adding_To_List[(16*w)-10][p]+Adding_To_List[(16*w)-9][p]+Adding_To_List[(16*w)-8][p]+Adding_To_List[(16*w)-7][p]+Adding_To_List[(16*w)-6][p]+Adding_To_List[(16*w)-5][p]+Adding_To_List[(16*w)-4][p]+Adding_To_List[(16*w)-3][p]+Adding_To_List[(16*w)-2][p]+Adding_To_List[(16*w)-1][p])
        for u in range(0,2):
            print(New_List[u])

    Output_Board(Current_Round) #function












red = Camel("RED") #global assignment
blue = Camel("BLUE")
green = Camel("GREEN")
yellow = Camel("YELLOW")
purple = Camel("PURPLE")
black = Camel("BLACK")
white = Camel("WHITE")

PLAY_GAME()

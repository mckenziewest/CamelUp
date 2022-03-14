
from builtins import float
import random
import pandas as pd
from csv import writer
import numpy as np
import os
import ast


def Output_Board(Round):
    x = [" _______  _______  _______  _______  _______  _______  _______  _______  _______  _______  _______  _______  _______  _______  _______  _______  _______",
         "    1        2        3        4        5        6        7        8        9        10       11       12       13       14       15       16     Winner"]
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

def Print_Out_Beginning_Board(Color_Dict, Current_Round, Color_Def_Dict):           #Function to print out starting data
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

def Print_Out_Final_Board(Color_Dict, Current_Round, Color_Def_Dict):   #function to print out final layout of board game
    Color_List = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "WHITE"]
    Adding_To_List = []
    for i in range(5,0, -1): #5,4,3,2,1 heights    
        for j in range(1,18): #1 - 17 spaces       
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
            New_List.append(Adding_To_List[(17*w)-17][p]+Adding_To_List[(17*w)-16][p]+Adding_To_List[(17*w)-15][p]+Adding_To_List[(17*w)-14][p]+Adding_To_List[(17*w)-13][p]+Adding_To_List[(17*w)-12][p]+Adding_To_List[(17*w)-11][p]+Adding_To_List[(17*w)-10][p]+Adding_To_List[(17*w)-9][p]+Adding_To_List[(17*w)-8][p]+Adding_To_List[(17*w)-7][p]+Adding_To_List[(17*w)-6][p]+Adding_To_List[(17*w)-5][p]+Adding_To_List[(17*w)-4][p]+Adding_To_List[(17*w)-3][p]+Adding_To_List[(17*w)-2][p]+Adding_To_List[(17*w)-1][p])
        for u in range(0,2):
            print(New_List[u])
    Output_Board(Current_Round) #function

def READ_IN_UPDATE_EXCEL_File():
    data = pd.read_csv('Camel_Up_Excel_Findings.csv')
    print(data)

    #read in data
    #append to dataset
    Number_of_Games = int(input("How many games would you like played: "))
    for a in range(0,Number_of_Games):
        PLAY_GAME()                                     #funtion to play our game

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

    def Set_Position(self, Number):
        self.position = Number

def ResetCamelClass(): #DONT TOUCH
    Color_List = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "WHITE"] 
    Color_Dict = {"RED":red, "BLUE":blue, "GREEN":green, "PURPLE":purple, "YELLOW":yellow, "BLACK":black, "WHITE":white}
    for camel in range(0,len(Color_List)):
        if (Color_List[camel] == "BLACK") or (Color_List[camel] == "WHITE"):
            Color_Dict[Color_List[camel]].Change_Camel_Above(None)
            Color_Dict[Color_List[camel]].Change_Camel_Below(None)
            Color_Dict[Color_List[camel]].Change_Height(1)
            Color_Dict[Color_List[camel]].Change_Position_B_or_W(-(17-Color_Dict[Color_List[camel]].position))
        else:
            Color_Dict[Color_List[camel]].Change_Camel_Above(None)
            Color_Dict[Color_List[camel]].Change_Camel_Below(None)
            Color_Dict[Color_List[camel]].Change_Height(1)
            Color_Dict[Color_List[camel]].Change_Position(-Color_Dict[Color_List[camel]].position)

def PLAY_GAME(): #DONE
    Color_List = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE"] 
    Color_Dict = {"RED":red, "BLUE":blue, "GREEN":green, "PURPLE":purple, "YELLOW":yellow, "BLACK":black, "WHITE":white}
    Color_Dict_CapLow = {'Blue':"BLUE", 'Red':"RED", 'Purple':"PURPLE", 'Yellow':"YELLOW", 'Green':"GREEN"}
    Color_Def_Dict = {
        "RED":Print_Red(), "BLUE":Print_Blue(), "GREEN":Print_Green(), "PURPLE":Print_Purple(), 
        "YELLOW":Print_Yellow(), "BLACK":Print_Black(), "WHITE":Print_White()
    } #never used anymore
    First_Dict = {                                                                        #Dict to reconize if spaces are taken
        1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 
        9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False
        }   
    Second_Dict = {                                                           #Dict for heights on each space
        1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 
        9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0
        }
    Printable_Array_List = []

    def OPTION_1_RANDOM_DATA(): #return Second_Dict
        First_Dict = {                                                                        #Dict to reconize if spaces are taken
            1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 
            9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False
        }
        Second_Dict = {                                                           #Dict for heights on each space
            1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 
            9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0
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
                First_Dict[17 - Rolled_Number] = True
                Second_Dict[17 - Rolled_Number] = Picked_Color.height

            else:
                Picked_Color.Change_Position_B_or_W(Rolled_Number)
                First_Dict[17 - Rolled_Number] = True
                Second_Dict[17 - Rolled_Number] = Picked_Color.height

        return Second_Dict

    def OPTION_2_INPUT_DATA(): #return Second_Dict
        NewListInput = """[['Blue', 'Red', 'Purple', 'Yellow', 'Green'], [3, 3, 2, 2, 2], [2, 1, 3, 2, 1]]
        for number in range(0,5):
            Color_Dict[Color_Dict_CapLow[NewListInput[0][number]]].Set_Position(NewListInput[1][number])
            Color_Dict[Color_Dict_CapLow[NewListInput[0][number]]].Change_Height(NewListInput[2][number])
            if number == 0:
                Color_Dict[Color_Dict_CapLow[NewListInput[0][number]]].Change_Camel_Above(None)
                if NewListInput[2][number] > 1:
                    Color_Dict[Color_Dict_CapLow[NewListInput[0][number]]].Change_Camel_Below(Color_Dict_CapLow[NewListInput[0][1]])
                else:
                    Color_Dict[Color_Dict_CapLow[NewListInput[0][number]]].Change_Camel_Below(None)
            elif number == 4:
                Color_Dict[Color_Dict_CapLow[NewListInput[0][number]]].Change_Camel_Below(None)
                if NewListInput[2][number-1] > 1:
                    Color_Dict[Color_Dict_CapLow[NewListInput[0][number]]].Change_Camel_Above(Color_Dict_CapLow[NewListInput[0][3]])
                else:
                    Color_Dict[Color_Dict_CapLow[NewListInput[0][number]]].Change_Camel_Above(None)
            else:
                if NewListInput[2][number] == 1:
                    Color_Dict[Color_Dict_CapLow[NewListInput[0][number]]].Change_Camel_Below(None)
                    if NewListInput[2][number-1] == 1:
                        Color_Dict[Color_Dict_CapLow[NewListInput[0][number]]].Change_Camel_Above(None)
                    else:
                        Color_Dict[Color_Dict_CapLow[NewListInput[0][number]]].Change_Camel_Above(Color_Dict_CapLow[NewListInput[0][number-1]])
                else:
                    Color_Dict[Color_Dict_CapLow[NewListInput[0][number]]].Change_Camel_Below(Color_Dict_CapLow[NewListInput[0][number+1]])
                    if NewListInput[2][number-1] == 1:
                        Color_Dict[Color_Dict_CapLow[NewListInput[0][number]]].Change_Camel_Above(None)
                    else:
                        Color_Dict[Color_Dict_CapLow[NewListInput[0][number]]].Change_Camel_Above(Color_Dict_CapLow[NewListInput[0][number-1]])

            First_Dict[NewListInput[1][number]] = True
            Second_Dict[NewListInput[2][number]] = 1 + Second_Dict[NewListInput[2][number]]"""


        First_Dict = {                   #delete                                                      #Dict to reconize if spaces are taken
            1:False, 2:True, 3:True, 4:False, 5:False, 6:False, 7:False, 8:False, 
            9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:True, 16:True, 17:False
        }
        Second_Dict = {                 #delete                                          #Dict for heights on each space
            1:0, 2:3, 3:2, 4:0, 5:0, 6:0, 7:0, 8:0, 
            9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:1, 16:1, 17:0
        } 
        red.Set_Position(3)
        red.Change_Height(1)
        red.Change_Camel_Above("BLUE")   #COLOR or None
        red.Change_Camel_Below(None)   #COLOR or None
    
        blue.Set_Position(3)
        blue.Change_Height(2)
        blue.Change_Camel_Above(None)  #COLOR or None
        blue.Change_Camel_Below("RED")  #COLOR or None

        green.Set_Position(2)
        green.Change_Height(1)
        green.Change_Camel_Above("YELLOW") #COLOR or None
        green.Change_Camel_Below(None) #COLOR or None

        purple.Set_Position(2)
        purple.Change_Height(3)
        purple.Change_Camel_Above(None) #COLOR or None
        purple.Change_Camel_Below("YELLOW") #COLOR or None
    
        yellow.Set_Position(2)
        yellow.Change_Height(2)
        yellow.Change_Camel_Above("PURPLE") #COLOR or None
        yellow.Change_Camel_Below("GREEN") #COLOR or None

        black.Set_Position(16)
        black.Change_Height(1)
        black.Change_Camel_Above(None) #COLOR or None
        black.Change_Camel_Below(None) #COLOR or None
        First_Dict[16] = True
        Second_Dict[16] = 1

        white.Set_Position(15)        #Starting positon 17
        white.Change_Height(1)          #Starting height is 1
        white.Change_Camel_Above(None) #COLOR or None
        white.Change_Camel_Below(None) #COLOR or None
        First_Dict[15] = True
        Second_Dict[15] = 1

        return Second_Dict

    #### CHANGEING RETURN INTO USEABLE First_Dict & Second_Dict ####

    #############################################
    #  PICK AN OPTION FOR INPUT                 #
    #   1) OPTION_1_RANDOM_DATA()               #
    #   2) OPTION_2_INPUT_DATA()                #
    #                                           #
    # OPTION 1) Sets a random game state        #
    # OPTION 2) Allows for a set game state     #
    #############################################

    Second_Dict = OPTION_2_INPUT_DATA() #Either OPTION_1_RANDOM_DATA() or OPTION_2_INPUT_DATA()

    for i in range(1, 18):
        if Second_Dict[i] != 0:
            First_Dict[i] = True

    #### APPENDING TO RETURN LIST ####

    Appeading_To_PAL =  [["Red", red.position, red.height], ["Blue", blue.position, blue.height], ["Green", green.position, green.height], ["Yellow", yellow.position, yellow.height], ["Purple", purple.position, purple.height]]
    Printable_Array_List.append(Appeading_To_PAL)

    #### ACTUALLY PLAYING THE GAME ####
    Current_Round = 0
    Winner_Found = False
    Done = False                                                                                    #SETTING UP HOW MANY GAMES 
    Number_of_Total_Roles = 0
    Number_Of_Rounds = 20     #int(input("How many rounds should we play: "))                        #EVERY 5 ROUNDS IS A ROUND
    for i in range(0,Number_Of_Rounds): #number of rounds played        COUNTS EACH ROUND
        Dice_List = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "B/W"] 
        for j in range(0,5): #number of dice rolled                     COUNTS EACH DICE ROLE
            Dice = random.choice(Dice_List) #string                     DICE COLOR
            Dice_List.remove(Dice)
            Number = random.randint(1,3) #1,2,3                  NUMBER ON DICE
            
            #print("\nRound Number: {:<5} Color Moved: {:<8}   Dice Number Rolled:  {:<5}   Roles Left: {:<5}".format(i,Dice, Number, 5-(j+1)))         #USED TO CHECK

            if Dice != "B/W":
                Color = Color_Dict[Dice]    
                Original_Camel_Position = Color.position 
                Color.Change_Position(Number) #new position

                if Color.position >= 17:                                #this finds winner if a camel reaches space 17 or greater
                    Difference_In_Pos = Color.position - 17
                    Color.Change_Position_B_or_W(Difference_In_Pos)
                    Winner_Found = True
                    Final_Round = Number_of_Total_Roles + 1             #plus one to account for this round as the calc is done before adding another 1
                    Done = True

                    #below is moving the rest of the camels down or into position
                    if Color.height == 1:                               #not changing heights
                        First_Dict[Original_Camel_Position] = False     #change old position of stack to empty
                        First_Dict[Color.position] = True               #change new position to occupied
                        Second_Dict[Color.position] = Second_Dict[Original_Camel_Position]
                        Second_Dict[Original_Camel_Position] = 0

                        while Color.camel_above != None:
                            New_Camel_Color = Color_Dict[Color.camel_above]
                            Color = New_Camel_Color
                            Color.Change_Position(Number)

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
                    break
            
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
                        Bottom_Of_Choice.Change_Camel_Above(None)                           #MAY BE ERROR

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

                    else: #height going down onto a camel               ERROR IN HERE SOMEWHERE
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
                                    Color.Change_Height(Other_Color.height +1) #changes the heights
                                    New_Camel_Color = Color_Dict[Color.camel_above] 
                                    Other_Color = Color
                                    Color = New_Camel_Color
                                    Color.Change_Position(Number)

                                if Color.camel_above == None:
                                    Color.Change_Height(Other_Color.height +1)

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
                        Change_In_Height = Second_Dict[Original_Camel_Position] - Second_Dict[Color.position] -1   #subtract from current height   
                        Color_Dict[Color.camel_below].Change_Camel_Above(None)  
                        Second_Dict[Color.position] += Second_Dict[Original_Camel_Position] - Color_Dict[Color.camel_below].height #CHECK  G
                        Second_Dict[Original_Camel_Position] = Color_Dict[Color.camel_below].height  

                        Dice_List_2 = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "WHITE"]              #next 6 lines cover camel_below and camel_above
                        for q in range(0,len(Dice_List_2)): #0,1,2,3,4, 5, 6
                            if (Color_Dict[Dice_List_2[q]].position == Color.position) and (Color_Dict[Dice_List_2[q]].camel_above == None) and (Color.color != Dice_List_2[q]): #find top of new stack
                                Color.Change_Camel_Below(Dice_List_2[q])  
                                Other_Color = Color_Dict[Dice_List_2[q]]
                                Other_Color.Change_Camel_Above(Color.color)  

                                while Color.camel_above != None:                         
                                    Color.Change_Height(Other_Color.height +1) #changes the heights
                                    New_Camel_Color = Color_Dict[Color.camel_above] 
                                    Other_Color = Color
                                    Color = New_Camel_Color
                                    Color.Change_Position_B_or_W(Number)

                                if Color.camel_above == None:
                                    Color.Change_Height(Other_Color.height +1)
                            
                        #Case (8)
            Number_of_Total_Roles += 1
        #add to Printable_Array_List to later add to array

        Appeading_To_PAL =  [["Red", red.position, red.height], ["Blue", blue.position, blue.height], ["Green", green.position, green.height], ["Yellow", yellow.position, yellow.height], ["Purple", purple.position, purple.height]]
        Printable_Array_List.append(Appeading_To_PAL)
        Current_Round += 1

        if Done == True:
            break


    Dice_List_2 = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "BLACK", "WHITE"]             
    if Winner_Found == True:
        while (Color.camel_above != None):                                                                  #finds top color
            Color = Color_Dict[Color.camel_above]
        Found_True_Color = False
        while Found_True_Color == False:                                            #elimitaing the top colors of being white or black
            if (Color.color == "BLACK") or (Color.color == "WHITE"):
                Color = Color_Dict[Color.camel_below]
            else:
                Found_True_Color = True
        #print("\nWinner Camel: {}     Number of Rounds: {}".format(Color.color, Final_Round))   
    return Printable_Array_List
    
def OrderingGameOutput(): #WORKS
    
    #### RESET ALL CAMEL VALUES ####
    ResetCamelClass()

    #### START TO PLAY GAMES ####
    List_From_Game = PLAY_GAME() #this is the list that is returned by PLAYGAME
    List_In_Order = []
    List_in_order_color = []
    List_in_order_position = []
    List_in_order_height = []
    for f in range(0,len(List_From_Game)): #where f is the number of rounds
        for h in range(0,5): #h is the elements of List_From_Game
            added = False
            for x in range(0,len(List_in_order_position)): #x is the number in List_in_order_position
                if List_From_Game[f][h][1] > List_in_order_position[x]:
                    if (List_From_Game[f][h][0] not in List_in_order_color):
                        List_in_order_position.insert(x, List_From_Game[f][h][1])
                        List_in_order_color.insert(x, List_From_Game[f][h][0])
                        List_in_order_height.insert(x, List_From_Game[f][h][2])
                        added = True
                        break
                elif List_From_Game[f][h][1] == List_in_order_position[x]:  #checks color vs each element in List_in_order_position
                    wordle = False  #check to make the element from List_From_Game was added
                    Number_of_Repeats = len([i for i,x in enumerate(List_in_order_position) if x==List_From_Game[f][h][1]])
                    #print("Number of repeats: "+ str(Number_of_Repeats))
                    for love in range(0,Number_of_Repeats): #checks how many repeat numbers are in List_in_order_position
                        if (List_From_Game[f][h][0] not in List_in_order_color):
                            if (List_From_Game[f][h][2] > List_in_order_height[x+love]) and (wordle == False):
                                List_in_order_position.insert(x+love, List_From_Game[f][h][1])
                                List_in_order_color.insert(x+love, List_From_Game[f][h][0])
                                List_in_order_height.insert(x+love, List_From_Game[f][h][2])
                                added = True
                                wordle = True
                                break
                    if (wordle == False) and (List_From_Game[f][h][0] not in List_in_order_color): #WORKS
                        List_in_order_position.insert(x+Number_of_Repeats, List_From_Game[f][h][1])
                        List_in_order_color.insert(x+Number_of_Repeats, List_From_Game[f][h][0])
                        List_in_order_height.insert(x+Number_of_Repeats, List_From_Game[f][h][2])
                        added = True
                        break
            if added == False: #WORKS 
                List_in_order_position.append(List_From_Game[f][h][1])
                List_in_order_color.append(List_From_Game[f][h][0])
                List_in_order_height.append(List_From_Game[f][h][2])
        List_In_Order.append([List_in_order_color, List_in_order_position, List_in_order_height])
        List_in_order_color = []
        List_in_order_position = []
        List_in_order_height = [] 
    #print(List_From_Game)
    #print(List_In_Order)
    return List_In_Order

def WriteToTXTFile(ListFromRound): #DONE
    Data = ListFromRound
    Data = str(Data)
    Path = "/Users/mattgilbert/Downloads/College/5th Year/Camel Up/Output_For_CamelUp.txt"      #Path chnaged based on computer
   
    with open(Path, "a") as file:
        file.writelines("\n")
        file.writelines(Data)

def NumberOfGamesRan(): #DONE
    Number = int(input("How many games should be played (ex. 3): "))
    for rounds in range(0,Number):
        WriteToTXTFile(OrderingGameOutput())

def RunOutputTXTFileProbability(): #returns probability #DONE
    CorrectOrientationList = []
    UserInputList = input("Starting position list such as [['Blue', 'Red', 'Purple', 'Yellow', 'Green'], [3, 3, 2, 2, 2], [2, 1, 3, 2, 1]]: ")
    UserInterestedColor = input("Color probability selection (Blue/Red/Purple/Yellow/Green): ")
    ChoosenColor = 5 #changed to 0 through 4
    ColorList = ['Blue', 'Red', 'Purple', 'Yellow', 'Green']
    StartingLetter = UserInterestedColor[0]
    for t in range(0,len(ColorList)):
        if ColorList[t] == UserInterestedColor:
            ChoosenColor = t

    Path = "/Users/mattgilbert/Downloads/College/5th Year/Camel Up/Output_For_CamelUp.txt" #Path chnaged based on computer
    with open(Path, "r") as file:
        for row in file: 
            if UserInputList in row:
                x = ast.literal_eval(row)
                CorrectOrientationList.append(x)
    
    #start finding the probability
    FoundToBeFirst = 0
    FoundToBeSecond = 0
    FoundToBeThirdOrHigher = 0
    TotalGamesAnalyzed = len(CorrectOrientationList)

    for row in range(0,len(CorrectOrientationList)):
        FirstSublist = CorrectOrientationList[row][0][0] #first list is game, then round, then individual list
        SecondSublist = CorrectOrientationList[row][1][0]
        OrderedWinnerList = [SecondSublist.index(FirstSublist[i]) for i in range(5)] #Example: [1, 0, 3, 4, 2]
        if OrderedWinnerList[ChoosenColor] == 0: #found to be first
            FoundToBeFirst += 1
        elif OrderedWinnerList[ChoosenColor] == 1: #found to be second
            FoundToBeSecond += 1
        else:
            FoundToBeThirdOrHigher += 1
    ExpectedValue = ["P({}=1) = {}".format(StartingLetter,FoundToBeFirst), "P({}=2) = {}".format(StartingLetter,FoundToBeSecond), "P({}>=3) = {}".format(StartingLetter,FoundToBeThirdOrHigher), "Total Games Analyzed: {}".format(TotalGamesAnalyzed)]
    #used for p(b=1)*2 + p(b=2)*1 + p(b>=3)*-1
    #return CorrectOrientationList
    return ExpectedValue

def CreateTable(InputList): #NOT DONE
    Headings = ["1st Place","2nd Place", "3rd Place", "4th Place", "5th PLace"]
    #### PUT ON HOLD, NOT AS USEFUL ANYMORE ####

 


#### GLOBAL ASSIGNMENT ####

red = Camel("RED")
blue = Camel("BLUE")
green = Camel("GREEN")
yellow = Camel("YELLOW")
purple = Camel("PURPLE")
black = Camel("BLACK")
white = Camel("WHITE")

#NumberOfGamesRan() # \\ RUNS GAMES
print(RunOutputTXTFileProbability())# \\ RUNS PROBABILITY

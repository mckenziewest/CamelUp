#Declaration of Variables for Dice and Distance calculation
red_Roll <- c("Red 1", "Red 2", "Red 3", "Red 1", "Red 2", "Red 3")

blue_Roll <- c("Blue 1", "Blue 2", "Blue 3", "Blue 1", "Blue 2", "Blue 3")

yellow_Roll <- c("Yellow 1", "Yellow 2", "Yellow 3", "Yellow 1", "Yellow 2", "Yellow 3")

green_Roll <- c("Green 1", "Green 2", "Green 3", "Green 1", "Green 2", "Green 3")

purple_Roll <- c("Purple 1", "Purple 2", "Purple 3", "Purple 1", "Purple 2", "Purple 3")

black_white_Roll <- c("Black 1", "Black 2", "Black 3", "White 1", "White 2", "White 3")

total_Dice <- c(sample(red_Roll, 1, replace = TRUE), sample(blue_Roll, 1, replace = TRUE), sample(yellow_Roll, 1, replace = TRUE), sample(green_Roll, 1, replace = TRUE), sample(purple_Roll, 1, replace = TRUE), sample(black_white_Roll, 1, replace = TRUE))
 
#Initial Positions
red_Position <- sample(red_Roll, 1)
blue_Position <- sample(blue_Roll, 1)
yellow_Position <- sample(yellow_Roll, 1)
green_Position <- sample(green_Roll, 1)
purple_Position <- sample(purple_Roll, 1)
bw_Position <- sample(black_white_Roll, 1)

red_Position
blue_Position
yellow_Position
green_Position
purple_Position
bw_Position
#The position of white is the same as black for positioning at the start
                                                                                                                                                                                                                          
#Leg 1
dice_One <- sample(total_Dice, 5)
roll_One <- dice_One[1]
roll_Two <- dice_One[2]
roll_Three <- dice_One[3]
roll_Four <- dice_One[4]
roll_Five <- dice_One[5]

roll_One
roll_Two
roll_Three
roll_Four
roll_Five

#Leg2
dice_Two <- sample(total_Dice, 5)
roll_Six <- dice_Two[1]
roll_Seven <- dice_Two[2]
roll_Eight <- dice_Two[3]
roll_Nine <- dice_Two[4]
roll_Ten <- dice_Two[5]

roll_Six
roll_Seven
roll_Eight
roll_Nine
roll_Ten

#Leg 3
dice_Three <- sample(total_Dice, 5)
roll_Eleven <- dice_Three[1]
roll_Twelve <- dice_Three[2]
roll_Thirteen <- dice_Three[3]
roll_Fourteen <- dice_Three[4]
roll_Fifteen <- dice_Three[5]

roll_Eleven
roll_Twelve
roll_Thirteen
roll_Fourteen
roll_Fifteen

#Leg 4
dice_Four <- sample(total_Dice, 5)
roll_Eleven <- dice_Four[1]
roll_Twelve <- dice_Four[2]
roll_Thirteen <- dice_Four[3]
roll_Fourteen <- dice_Four[4]
roll_Fifteen <- dice_Four[5]

roll_Eleven
roll_Twelve
roll_Thirteen
roll_Fourteen
roll_Fifteen

#Leg 5
dice_Five<- sample(total_Dice, 5)
roll_Sixteen <- dice_Five[1]
roll_Seventeen <- dice_Five[2]
roll_Eighteen <- dice_Five[3]
roll_Nineteen <- dice_Five[4]
roll_Twemty <- dice_Five[5]

roll_Sixteen
roll_Seventeen
roll_Eighteen
roll_Nineteen
roll_Twenty

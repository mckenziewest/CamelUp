B <- 100
nLegs <- 1
red_Dice <- c(1, 1, 2, 2, 3, 3)
blue_Dice <- c(1, 1, 2, 2, 3, 3)
yellow_Dice <- c(1, 1, 2, 2, 3, 3)
green_Dice <- c(1, 1, 2, 2, 3, 3)
purple_Dice <- c(1, 1, 2, 2, 3, 3)
black_white_Dice <- c(1, 1, 2, 2, 3, 3)
black_Dice <- c(1, 2, 3)
white_Dice <- c(1, 2, 3)
black_White <- c("Black", "White")

red_Position <- 0
blue_Position <- 0
yellow_Position <- 0
green_Position <- 0
purple_Position <- 0
black_Position <- 0
white_Position <- 0

total_Dice <- c("red", "blue", "yellow", "green", "purple", "black and white") 

#Starting Positions
red_Position <- red_Position + sample(red_Dice, 1, replace = TRUE)
blue_Position <- blue_Position + sample(blue_Dice, 1, replace = TRUE)
yellow_Position <- yellow_Position + sample(yellow_Dice, 1, replace = TRUE)
green_Position <- green_Position + sample(green_Dice, 1, replace = TRUE)
purple_Position <- purple_Position + sample(purple_Dice, 1, replace = TRUE)
black_Position <- black_Position + 16 - sample(black_Dice, 1, replace = TRUE)
white_Position <- white_Position + 16 - sample(white_Dice, 1, replace = TRUE)
leg_Rolls <- sample(total_Dice, 5, replace = FALSE)

print("Here are the starting positions for the camels\n")
cat("Red Camel starts at space: ", red_Position)
cat("\nBlue Camel starts at space: ", blue_Position)
cat("\nYellow Camel starts at space: ", yellow_Position)
cat("\nGreen Camel starts at space: ", green_Position)
cat("\nPurple Camel starts at space: ", purple_Position)
cat("\nBlack Camel starts at space: ", black_Position)
cat("\nWhite Camel starts at space: ", white_Position)

#Board Game Dice Simulation in a while loop
while (red_Position < 17 && blue_Position < 17 && yellow_Position < 17 && green_Position < 17 && purple_Position < 17) {
  print("\n")
  cat("\nStart of Leg ", nLegs)
  print("\n")
  
  leg_Rolls[1]
  if (leg_Rolls[1] == "red") {
    red_Roll <- sample(red_Dice, 1, replace = TRUE)
    cat("\nRed Camel move: ", red_Roll)
    red_Position <- red_Position + red_Roll
    cat("\nRed Camel is on space: ", red_Position)
    
  } else if (leg_Rolls[1] == "blue") {
    blue_Roll <- sample(blue_Dice, 1, replace = TRUE)
    cat("\nBlue Camel move: ", blue_Roll)
    blue_Position <- blue_Position + blue_Roll
    cat("\nBlue Camel is on space: ", blue_Position)
    
  } else if (leg_Rolls[1] == "yellow") {
    yellow_Roll <- sample(yellow_Dice, 1, replace = TRUE)
    cat("\nYellow Camel move: ", yellow_Roll)
    yellow_Position <- yellow_Position + yellow_Roll
    cat("\nYellow Camel is on space: ", yellow_Position)
    
  } else if (leg_Rolls[1] == "green") {
    green_Roll <- sample(green_Dice, 1, replace = TRUE)
    cat("\nGreen Camel move: ", green_Roll)
    green_Position <- green_Position + green_Roll
    cat("\nGreen Camel is on space: ", green_Position)
    
  } else if (leg_Rolls[1] == "purple") {
    purple_Roll <- sample(purple_Dice, 1, replace = TRUE)
    cat("\nPurple Camel move: ", purple_Roll)
    purple_Position <- purple_Position + purple_Roll
    cat("\nPurple Camel is on space: ", purple_Position)
    
  } else if (leg_Rolls[1] == "black and white") {
    black_white_Roll <- sample(black_White, 1, replace = TRUE)
    if (black_white_Roll == "Black") {
      black_Roll <- sample(black_Dice, 1, replace = TRUE)
      cat("\nBlack Camel move: ", black_Roll)
      black_Position <- black_Position - black_Roll
      cat("\nBlack Camel is on space: ", black_Position)
    } else if (black_white_Roll == "White"){
      white_Roll <- sample(white_Dice, 1, replace = TRUE)
      cat("\nWhite Camel move: ", white_Roll)
      white_Position <- white_Position - white_Roll
      cat("\nWhite Camel is on space: ", white_Position)
    }
  }
  
  leg_Rolls[2]
  if (leg_Rolls[2] == "red") {
    red_Roll <- sample(red_Dice, 1, replace = TRUE)
    cat("\nRed Camel move: ", red_Roll)
    red_Position <- red_Position + red_Roll
    cat("\nRed Camel is on space: ", red_Position)
    
  } else if (leg_Rolls[2] == "blue") {
    blue_Roll <- sample(blue_Dice, 1, replace = TRUE)
    cat("\nBlue Camel move: ", blue_Roll)
    blue_Position <- blue_Position + blue_Roll
    cat("\nBlue Camel is on space: ", blue_Position)
    
  } else if (leg_Rolls[2] == "yellow") {
    yellow_Roll <- sample(yellow_Dice, 1, replace = TRUE)
    cat("\nYellow Camel move: ", yellow_Roll)
    yellow_Position <- yellow_Position + yellow_Roll
    cat("\nYellow Camel is on space: ", yellow_Position)
    
  } else if (leg_Rolls[2] == "green") {
    green_Roll <- sample(green_Dice, 1, replace = TRUE)
    cat("\nGreen Camel move: ", green_Roll)
    green_Position <- green_Position + green_Roll
    cat("\nGreen Camel is on space: ", green_Position)
    
  } else if (leg_Rolls[2] == "purple") {
    purple_Roll <- sample(purple_Dice, 1, replace = TRUE)
    cat("\nPurple Camel move: ", purple_Roll)
    purple_Position <- purple_Position + purple_Roll
    cat("\nPurple Camel is on space: ", purple_Position)
    
  } else if (leg_Rolls[2] == "black and white") {
    black_white_Roll <- sample(black_White, 1, replace = TRUE)
    if (black_white_Roll == "Black") {
      black_Roll <- sample(black_Dice, 1, replace = TRUE)
      cat("\nBlack Camel move: ", black_Roll)
      black_Position <- black_Position - black_Roll
      cat("\nBlack Camel is on space: ", black_Position)
    } else if (black_white_Roll == "White"){
      white_Roll <- sample(white_Dice, 1, replace = TRUE)
      cat("\nWhite Camel move: ", white_Roll)
      white_Position <- white_Position - white_Roll
      cat("\nWhite Camel is on space: ", white_Position)
    }
  }
  
  leg_Rolls[3]
  if (leg_Rolls[3] == "red") {
    red_Roll <- sample(red_Dice, 1, replace = TRUE)
    cat("\nRed Camel move: ", red_Roll)
    red_Position <- red_Position + red_Roll
    cat("\nRed Camel is on space: ", red_Position)
    
  } else if (leg_Rolls[3] == "blue") {
    blue_Roll <- sample(blue_Dice, 1, replace = TRUE)
    cat("\nBlue Camel move: ", blue_Roll)
    blue_Position <- blue_Position + blue_Roll
    cat("\nBlue Camel is on space: ", blue_Position)
    
  } else if (leg_Rolls[3] == "yellow") {
    yellow_Roll <- sample(yellow_Dice, 1, replace = TRUE)
    cat("\nYellow Camel move: ", yellow_Roll)
    yellow_Position <- yellow_Position + yellow_Roll
    cat("\nYellow Camel is on space: ", yellow_Position)
    
  } else if (leg_Rolls[3] == "green") {
    green_Roll <- sample(green_Dice, 1, replace = TRUE)
    cat("\nGreen Camel move: ", green_Roll)
    green_Position <- green_Position + green_Roll
    cat("\nGreen Camel is on space: ", green_Position)
    
  } else if (leg_Rolls[3] == "purple") {
    purple_Roll <- sample(purple_Dice, 1, replace = TRUE)
    cat("\nPurple Camel move: ", purple_Roll)
    purple_Position <- purple_Position + purple_Roll
    cat("\nPurple Camel is on space: ", purple_Position)
    
  } else if (leg_Rolls[3] == "black and white") {
    black_white_Roll <- sample(black_White, 1, replace = TRUE)
    if (black_white_Roll == "Black") {
      black_Roll <- sample(black_Dice, 1, replace = TRUE)
      cat("\nBlack Camel move: ", black_Roll)
      black_Position <- black_Position - black_Roll
      cat("\nBlack Camel is on space: ", black_Position)
    } else if (black_white_Roll == "White"){
      white_Roll <- sample(white_Dice, 1, replace = TRUE)
      cat("\nWhite Camel move: ", white_Roll)
      white_Position <- white_Position - white_Roll
      cat("\nWhite Camel is on space: ", white_Position)
    }
  }
  
  leg_Rolls[4]
  if (leg_Rolls[4] == "red") {
    red_Roll <- sample(red_Dice, 1, replace = TRUE)
    cat("\nRed Camel move: ", red_Roll)
    red_Position <- red_Position + red_Roll
    cat("\nRed Camel is on space: ", red_Position)
    
  } else if (leg_Rolls[4] == "blue") {
    blue_Roll <- sample(blue_Dice, 1, replace = TRUE)
    cat("\nBlue Camel move: ", blue_Roll)
    blue_Position <- blue_Position + blue_Roll
    cat("\nBlue Camel is on space: ", blue_Position)
    
  } else if (leg_Rolls[4] == "yellow") {
    yellow_Roll <- sample(yellow_Dice, 1, replace = TRUE)
    cat("\nYellow Camel move: ", yellow_Roll)
    yellow_Position <- yellow_Position + yellow_Roll
    cat("\nYellow Camel is on space: ", yellow_Position)
    
  } else if (leg_Rolls[4] == "green") {
    green_Roll <- sample(green_Dice, 1, replace = TRUE)
    cat("\nGreen Camel move: ", green_Roll)
    green_Position <- green_Position + green_Roll
    cat("\nGreen Camel is on space: ", green_Position)
    
  } else if (leg_Rolls[4] == "purple") {
    purple_Roll <- sample(purple_Dice, 1, replace = TRUE)
    cat("\nPurple Camel move: ", purple_Roll)
    purple_Position <- purple_Position + purple_Roll
    cat("\nPurple Camel is on space: ", purple_Position)
    
  } else if (leg_Rolls[4] == "black and white") {
    black_white_Roll <- sample(black_White, 1, replace = TRUE)
    if (black_white_Roll == "Black") {
      black_Roll <- sample(black_Dice, 1, replace = TRUE)
      cat("\nBlack Camel move: ", black_Roll)
      black_Position <- black_Position - black_Roll
      cat("\nBlack Camel is on space: ", black_Position)
    } else if (black_white_Roll == "White"){
      white_Roll <- sample(white_Dice, 1, replace = TRUE)
      cat("\nWhite Camel move: ", white_Roll)
      white_Position <- white_Position - white_Roll
      cat("\nWhite Camel is on space: ", white_Position)
    }
  }
  
  leg_Rolls[5]
  if (leg_Rolls[5] == "red") {
    red_Roll <- sample(red_Dice, 1, replace = TRUE)
    cat("\nRed Camel move: ", red_Roll)
    red_Position <- red_Position + red_Roll
    cat("\nRed Camel is on space: ", red_Position)
    
  } else if (leg_Rolls[5] == "blue") {
    blue_Roll <- sample(blue_Dice, 1, replace = TRUE)
    cat("\nBlue Camel move: ", blue_Roll)
    blue_Position <- blue_Position + blue_Roll
    cat("\nBlue Camel is on space: ", blue_Position)
    
  } else if (leg_Rolls[5] == "yellow") {
    yellow_Roll <- sample(yellow_Dice, 1, replace = TRUE)
    cat("\nYellow Camel move: ", yellow_Roll)
    yellow_Position <- yellow_Position + yellow_Roll
    cat("\nYellow Camel is on space: ", yellow_Position)
    
  } else if (leg_Rolls[5] == "green") {
    green_Roll <- sample(green_Dice, 1, replace = TRUE)
    cat("\nGreen Camel move: ", green_Roll)
    green_Position <- green_Position + green_Roll
    cat("\nGreen Camel is on space: ", green_Position)
    
  } else if (leg_Rolls[5] == "purple") {
    purple_Roll <- sample(purple_Dice, 1, replace = TRUE)
    cat("\nPurple Camel move: ", purple_Roll)
    purple_Position <- purple_Position + purple_Roll
    cat("\nPurple Camel is on space: ", purple_Position)
    
  } else if (leg_Rolls[5] == "black and white") {
    black_white_Roll <- sample(black_White, 1, replace = TRUE)
    if (black_white_Roll == "Black") {
      black_Roll <- sample(black_Dice, 1, replace = TRUE)
      cat("\nBlack Camel move: ", black_Roll)
      black_Position <- black_Position - black_Roll
      cat("\nBlack Camel is on space: ", black_Position)
    } else if (black_white_Roll == "White"){
      white_Roll <- sample(white_Dice, 1, replace = TRUE)
      cat("\nWhite Camel move: ", white_Roll)
      white_Position <- white_Position - white_Roll
      cat("\nWhite Camel is on space: ", white_Position)
    }
  }

  cat("\nEnd of Leg ", nLegs)
  print("\n")
  cat("\nHere are the Camel positions after Leg ", nLegs)
  
  cat("\nRed Camel: ", red_Position)
  cat("\nBlue Camel: ", blue_Position)
  cat("\nYellow Camel: ", yellow_Position)
  cat("\nGreen Camel: ", green_Position)
  cat("\nPurple Camel: ", purple_Position)
  cat("\nBlack Camel: ", black_Position)
  cat("\nWhite Camel: ", white_Position)
  
  nLegs = nLegs + 1
  leg_Rolls <- sample(total_Dice, 5, replace = FALSE)
}

#Final positions of all Camels
print("Here are the final positions of each camel/n")
cat("Red Camel: ", red_Position)
cat("\nBlue Camel: ", blue_Position)
cat("\nYellow Camel: ", yellow_Position)
cat("\nGreen Camel: ", green_Position)
cat("\nPurple Camel: ", purple_Position)
cat("\nBlack Camel: ", black_Position)
cat("\nWhite Camel: ", white_Position)

final_Position <- c(red_Position, blue_Position, yellow_Position, green_Position, purple_Position)
final_Rankings <- order(-final_Position)
final_Rankings

camelUp_Sim

replicate(B, camelUp_Sim)

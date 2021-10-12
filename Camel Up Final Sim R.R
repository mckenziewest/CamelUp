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

#Board Game Dice Simulation
while (red_Position < 17 && blue_Position < 17 && yellow_Position < 17 && green_Position < 17 && purple_Position < 17) {
  print("\n")
  cat("\nStart of Leg ", nLegs)
  print("\n")
  
  leg_Rolls[1]
  if (leg_Rolls[1] == "red") {
    cat("Red Camel move: ", sample(red_Dice, 1, replace = TRUE))
    red_Position <- red_Position + sample(red_Dice, 1, replace = TRUE)
    cat("\nRed Camel is on space: ", red_Position)
    
  } else if (leg_Rolls[1] == "blue") {
    cat("\nBlue Camel move: ", sample(blue_Dice, 1, replace = TRUE))
    blue_Position <- blue_Position + sample(blue_Dice, 1, replace = TRUE)
    cat("\nBlue Camel is on space: ", blue_Position)
    
  } else if (leg_Rolls[1] == "yellow") {
    cat("\nYellow Camel move: ", sample(yellow_Dice, 1, replace = TRUE))
    yellow_Position <- yellow_Position + sample(yellow_Dice, 1, replace = TRUE)
    cat("\nYellow Camel is on space: ", yellow_Position)
    
  } else if (leg_Rolls[1] == "green") {
    cat("\nGreen Camel move: ", sample(green_Dice, 1, replace = TRUE))
    green_Position <- green_Position + sample(green_Dice, 1, replace = TRUE)
    cat("\nGreen Camel is on space: ", green_Position)
    
  } else if (leg_Rolls[1] == "purple") {
    cat("\nPurple Camel move: ", sample(purple_Dice, 1, replace = TRUE))
    purple_Position <- purple_Position + sample(purple_Dice, 1, replace = TRUE)
    cat("\nPurple Camel is on space: ", purple_Position)
    
  } else if (leg_Rolls[1] == "black and white") {
    sample(black_White, 1, replace = TRUE)
    if (sample(black_White, 1, replace = TRUE) == "Black") {
      cat("\nBlack Camel move: ", sample(black_Dice, 1, replace = TRUE))
      black_Position <- black_Position - sample(black_Dice, 1, replace = TRUE)
      cat("\nBlack Camel is on space: ", black_Position)
    } else if (sample(black_White, 1, replace = TRUE) == "White"){
      cat("\nWhite Camel move: ", sample(white_Dice, 1, replace = TRUE))
      white_Position <- white_Position - sample(white_Dice, 1, replace = TRUE)
      cat("\nWhite Camel is on space: ", white_Position)
    }
  }
  
  leg_Rolls[2]
  if (leg_Rolls[2] == "red") {
    cat("\nRed Camel move: ", sample(red_Dice, 1, replace = TRUE))
    red_Position <- red_Position + sample(red_Dice, 1, replace = TRUE)
    cat("\nRed Camel is on space: ", red_Position)
    
  } else if (leg_Rolls[2] == "blue") {
    cat("\nBlue Camel move: ", sample(blue_Dice, 1, replace = TRUE))
    blue_Position <- blue_Position + sample(blue_Dice, 1, replace = TRUE)
    cat("\nBlue Camel is on space: ", blue_Position)
    
  } else if (leg_Rolls[2] == "yellow") {
    cat("\nYellow Camel move: ", sample(yellow_Dice, 1, replace = TRUE))
    yellow_Position <- yellow_Position + sample(yellow_Dice, 1, replace = TRUE)
    cat("\nYellow Camel is on space: ", yellow_Position)
    
  } else if (leg_Rolls[2] == "green") {
    cat("\nGreen Camel move: ", sample(green_Dice, 1, replace = TRUE))
    green_Position <- green_Position + sample(green_Dice, 1, replace = TRUE)
    cat("\nGreen Camel is on space: ", green_Position)
    
  } else if (leg_Rolls[2] == "purple") {
    cat("\nPurple Camel move: ", sample(purple_Dice, 1, replace = TRUE))
    purple_Position <- purple_Position + sample(purple_Dice, 1, replace = TRUE)
    cat("\nPurple Camel is on space: ", purple_Position)
    
  } else if (leg_Rolls[2] == "black and white") {
    sample(black_White, 1, replace = TRUE)
    if (sample(black_White, 1, replace = TRUE) == "Black") {
      cat("\nBlack Camel move: ", sample(black_Dice, 1, replace = TRUE))
      black_Position <- black_Position - sample(black_Dice, 1, replace = TRUE)
      cat("\nBlack Camel is on space: ", black_Position)
    } else if (sample(black_White, 1, replace = TRUE) == "White") {
      cat("\nWhite Camel move: ", sample(white_Dice, 1, replace = TRUE))
      white_Position <- white_Position - sample(white_Dice, 1, replace = TRUE)
      cat("\nWhite Camel is on space: ", white_Position)
    }
  }
  
  leg_Rolls[3]
  if (leg_Rolls[3] == "red") {
    cat("\nRed Camel move: ", sample(red_Dice, 1, replace = TRUE))
    red_Position <- red_Position + sample(red_Dice, 1, replace = TRUE)
    cat("\nRed Camel is on space: ", red_Position)
    
  } else if (leg_Rolls[3] == "blue") {
    cat("\nBlue Camel move: ", sample(blue_Dice, 1, replace = TRUE))
    blue_Position <- blue_Position + sample(blue_Dice, 1, replace = TRUE)
    cat("\nBlue Camel is on space: ", blue_Position)
    
  } else if (leg_Rolls[3] == "yellow") {
    cat("\nYellow Camel move: ", sample(yellow_Dice, 1, replace = TRUE))
    yellow_Position <- yellow_Position + sample(yellow_Dice, 1, replace = TRUE)
    cat("\nYellow Camel is on space: ", yellow_Position)
    
  } else if (leg_Rolls[3] == "green") {
    cat("\nGreen Camel move: ", sample(green_Dice, 1, replace = TRUE))
    green_Position <- green_Position + sample(green_Dice, 1, replace = TRUE)
    cat("\nGreen Camel is on space: ", green_Position)
    
  } else if (leg_Rolls[3] == "purple") {
    cat("\nPurple Camel move: ", sample(purple_Dice, 1, replace = TRUE))
    purple_Position <- purple_Position + sample(purple_Dice, 1, replace = TRUE)
    cat("\nPurple Camel is on space: ", purple_Position)
    
  } else if (leg_Rolls[3] == "black and white") {
    sample(black_White, 1, replace = TRUE)
    if (sample(black_White, 1, replace = TRUE) == "Black") {
      cat("\nBlack Camel move: ", sample(black_Dice, 1, replace = TRUE))
      black_Position <- black_Position - sample(black_Dice, 1, replace = TRUE)
      cat("\nBlack Camel is on space: ", black_Position)
    } else if (sample(black_White, 1, replace = TRUE) == "White") {
      cat("\nWhite Camel move: ", sample(white_Dice, 1, replace = TRUE))
      white_Position <- white_Position - sample(white_Dice, 1, replace = TRUE)
      cat("\nWhite Camel is on space: ", white_Position)
    }
  }
  
  leg_Rolls[4]
  if (leg_Rolls[4] == "red") {
    cat("\nRed Camel move: ", sample(red_Dice, 1, replace = TRUE))
    red_Position <- red_Position + sample(red_Dice, 1, replace = TRUE)
    cat("\nRed Camel is on space: ", red_Position)
    
  } else if (leg_Rolls[4] == "blue") {
    cat("\nBlue Camel move: ", sample(blue_Dice, 1, replace = TRUE))
    blue_Position <- blue_Position + sample(blue_Dice, 1, replace = TRUE)
    cat("\nBlue Camel is on space: ", blue_Position)
    
  } else if (leg_Rolls[4] == "yellow") {
    cat("\nYellow Camel move: ", sample(yellow_Dice, 1, replace = TRUE))
    yellow_Position <- yellow_Position + sample(yellow_Dice, 1, replace = TRUE)
    cat("\nYellow Camel is on space: ", yellow_Position)
    
  } else if (leg_Rolls[4] == "green") {
    cat("\nGreen Camel move: ", sample(green_Dice, 1, replace = TRUE))
    green_Position <- green_Position + sample(green_Dice, 1, replace = TRUE)
    cat("\nGreen Camel is on space: ", green_Position)
    
  } else if (leg_Rolls[4] == "purple") {
    cat("\nPurple Camel move: ", sample(purple_Dice, 1, replace = TRUE))
    purple_Position <- purple_Position + sample(purple_Dice, 1, replace = TRUE)
    cat("\nPurple Camel is on space: ", purple_Position)
    
  } else if (leg_Rolls[4] == "black and white") {
    sample(black_White, 1, replace = TRUE)
    
    if (sample(black_White, 1, replace = TRUE) == "Black") {
      cat("\nBlack Camel move: ", sample(black_Dice, 1, replace = TRUE))
      black_Position <- black_Position - sample(black_Dice, 1, replace = TRUE)
      cat("\nBlack Camel is on space: ", black_Position)
    } else if (sample(black_White, 1, replace = TRUE) == "White") {
      cat("\nWhite Camel move: ", sample(white_Dice, 1, replace = TRUE))
      white_Position <- white_Position - sample(white_Dice, 1, replace = TRUE)
      cat("\nWhite Camel is on space: ", white_Position)
    }
  }
  
  leg_Rolls[5]
  if (leg_Rolls[5] == "red") {
    cat("\nRed Camel move: ", sample(red_Dice, 1, replace = TRUE))
    red_Position <- red_Position + sample(red_Dice, 1, replace = TRUE)
    cat("\nRed Camel is on space: ", red_Position)
    
  } else if (leg_Rolls[5] == "blue") {
    cat("\nBlue Camel move: ", sample(blue_Dice, 1, replace = TRUE))
    blue_Position <- blue_Position + sample(blue_Dice, 1, replace = TRUE)
    cat("\nBlue Camel is on space: ", blue_Position)
    
  } else if (leg_Rolls[5] == "yellow") {
    cat("\nYellow Camel move: ", sample(yellow_Dice, 1, replace = TRUE))
    yellow_Position <- yellow_Position + sample(yellow_Dice, 1, replace = TRUE)
    cat("\nYellow Camel is on space: ", yellow_Position)
    
  } else if (leg_Rolls[5] == "green") {
    cat("\nGreen Camel move: ", sample(green_Dice, 1, replace = TRUE))
    green_Position <- green_Position + sample(green_Dice, 1, replace = TRUE)
    cat("\nGreen Camel is on space: ", green_Position)
    
  } else if (leg_Rolls[5] == "purple") {
    cat("\nPurple Camel move: ", sample(purple_Dice, 1, replace = TRUE))
    purple_Position <- purple_Position + sample(purple_Dice, 1, replace = TRUE)
    cat("\nPurple Camel is on space: ", purple_Position)
    
  } else if (leg_Rolls[5] == "black and white") {
    sample(black_White, 1, replace = TRUE)
    
    if (sample(black_White, 1, replace = TRUE) == "Black") {
      cat("\nBlack Camel move: ", sample(black_Dice, 1, replace = TRUE))
      black_Position <- black_Position - sample(black_Dice, 1, replace = TRUE)
      cat("\nBlack Camel is on space: ", black_Position)
    } else if (sample(black_White, 1, replace = TRUE) == "White") {
      cat("\nWhite Camel move: ", sample(white_Dice, 1, replace = TRUE))
      white_Position <- white_Position - sample(white_Dice, 1, replace = TRUE)
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
  
  nLegs = nLegs + 1
}

print("Here are the final positions of each camel/n")
cat("Red Camel: ", red_Position)
cat("\nBlue Camel: ", blue_Position)
cat("\nYellow Camel: ", yellow_Position)
cat("\nGreen Camel: ", green_Position)
cat("\nPurple Camel: ", purple_Position)

final_Position <- c(red_Position, blue_Position, yellow_Position, green_Position, purple_Position)
final_Rankings <- order(-final_Position)
final_Rankings

camelUp_Sim

replicate(B, camelUp_Sim)


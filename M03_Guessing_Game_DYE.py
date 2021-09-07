#import these modules to use in the program.
#random allows us to use commands to generate random numbers.
#is_num verifies that the user actually inputs a number instead of a string.

import random
from is_num import is_num

#generate a random integer between 1 and 100
randy = random.randint(1, 100)

#turn variable to keep track of the user's turns
#question variable to ask the user if they want to play again
question = "y"
while question == "y" or question == "":
    question = input("Would you like to play again? Y|n: ").lower()
    turn = 0

    while turn < 5:
        print("You have " + str(5 - turn) + " turns left.")
        userguess = is_num("Guess a number between 1 and 100: ")
        if userguess > 100:
            print("Please input a number between 1 and 100.")
            continue
        elif userguess < 1:
            print("Please input a number between 1 and 100.")
        elif (randy == userguess):
            print("You win!")
            break
        elif randy > userguess:
            turn+=1
            print("Your guess is too low, try again")
        elif randy < userguess:
            turn+=1
            print("Your guess is too high, try again")
    print("You lose.")

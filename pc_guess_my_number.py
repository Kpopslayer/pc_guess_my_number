# player picks a number between 1 and 100
# the computer guesses by using random.randint(1, 100) function
# the guess from the computer is displayed
# each try is counted
# when the computer is succesful, the number of tries is printed

# import random module
import random

# intro
print("\t\t\tLet the computer guess your number!")

# initial values
# player picks a number
# don't forget to convert the input to an integer
number = int(input("\npick a number between 1 and 100: "))
guess = 0
tries = 0

# guessing loop
while guess != number:
    guess = random.randint(1, 100)
    print("Is it...", guess,"?")
    tries += 1
    
# number of tries is printed
print("\nIt took the computer", tries, "tries.")

# exiting the program
input("\n\nPress the enter key to exit the program.")
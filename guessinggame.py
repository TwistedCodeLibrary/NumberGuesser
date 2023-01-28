#Guessing Game with guess count
#guessinggame.py
#Last edited Sept. 29 2020 by Aaron Ndow for CSCI 111

#enables random outputs
import random
import time

#declare variables

guess = 0.0

count = 0 #counts the number of guesses

RandomNumber = random.randint(1,100) #selects number to guess

#Inputs guess
while guess != RandomNumber:
    
    guess = int(input("Pick a number from 1 to 100:"))
    #Shows that number is too low
    if guess < RandomNumber:
        count += 1
        print("Too low!")

    #Shows that number is too high
    elif guess > RandomNumber:
        count += 1
        print("Too high!")

    #Shows that number is equal
    elif guess == RandomNumber:
        count += 1
        print("Good job! The number was " + str(RandomNumber) + ". It took you " + str(count) + " guesses.")

    #Ends the script
        time.sleep(5)
        break 
    

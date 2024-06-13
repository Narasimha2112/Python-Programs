#import random and time module
import random
import time

#Create a random number b/w 1 to 100
n = random.randrange(1,100)  

#Write a welcome message
print("Welcome to the Number Guessing Game \n Yo have only 5 attempts to guess")

#give 3.sec delay
time.sleep(3)

#take a user input to enter a number
guess = int(input("Guess a number : "))

#use while loop and create a condition which execute while loop till the both number not become equal
#if n is not equal to the guess

count = 1
while n != guess and count<5:   
    #if guess is smaller than n
    if guess<n:
        print("Too Low")
        print("You have {} attempts left".format((5-count)))
        guess = int(input("Guess Again : "))
        count += 1
    #if guess is greater than n
    elif guess>n:
        print("Too High")
        print("You have {} attempts left".format((5-count)))
        guess = int(input("Guess Again : "))
        count += 1
    #if guess get equals to n terminate the while loop
    else:
        break
#final message
if n == guess:
    print(" ***  You guessed it right *** ")
else:
    print("Bad Luck , Try again..!")
    
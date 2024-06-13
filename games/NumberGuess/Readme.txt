Number Guessing Game Theory Part

Number Guessing Game

This script is an interactive guessing game, which will ask the user to guess a number between 1 and 99.

We are using the time and random module with the randrange() method to get a random number. The script also contains a while loop, which make the script run until the user guess the right number.

In this basic project you will learn to use random module, time module, if elif statement, while loop etc.



Now lets talk about how we are going to create this number guessing game

1. we import random and time module

2. we use random module method 'randrange()' to get a randomly selected number from the specified range (1 to 20) and store it to a variable.

3. we use time module function "sleep()" this sleep() is used to put program to sleep for given amount of seconds as argument.

4. we take a input from user as it guess and store it into a variable.

5. Now we use while loop were we check or compare user guessed number and randomly selected number if both number were not equal then we compare those two number again using if elif statement and tell user to guess new number again and this step continues until user guessed the same number. 

6. when user guessed number and randomly selected number are matched we get the message " **  you guessed it right!!  ** "

After completing this game we are going to add some more functionality like user only have 5 attempts to guess the number.
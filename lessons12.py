# This is a guess the number game.
import random

print('Hello, what is your name?')
name = input()

print('Well, ' + name + ', I\'m thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7): # this will give the user exactly 6 attempts to guess the number.
    print("Take a guess.")
    guess = int(input()) # we need to include "int" to ensure we are comparing an interteger, (and not a str) input to the random.randint created above

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess!

if int(guess) == secretNumber:
    print("Good job " + name + '! you guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
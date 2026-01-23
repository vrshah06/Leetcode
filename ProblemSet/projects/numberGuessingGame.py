lower = input("Enter the lower bound: ")
upper = input("Enter the upper bound: ")
print("You have to guess a number between " + lower + " and " + upper)
import random
num = random.randint(int(lower), int(upper))
guess = None
while guess != num:
    guess = input("Enter your guess: ")
    if int(guess) < num:
        print("Too low! Try again.")
    elif int(guess) > num:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number.")
import random

print("Number guessing game")

daNumber = random.randint(1, 9)

chances = 0

print("Guess a number (between 1 and 9):")

while chances < 5:

    guess = int(input("Enter Da Number:- "))


    if guess == daNumber:
        
        print("Congratulation YOU WON!!!")
        break

    elif guess < daNumber:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

    chances += 1

if not chances < 5:
    print("YOU LOSE!!! The number is", daNumber)
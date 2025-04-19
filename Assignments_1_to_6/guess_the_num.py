import random

def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    print(f"I'm thinking of a number between 1 and {x}... Can you guess it? 😉")
    
    while guess != random_num:
        try:
            guess = int(input("Enter your guess: "))
            if guess < random_num:
                print("Too low! Try again.")
            elif guess > random_num:
                print("Too high! Try again.")
        except ValueError:
            print("Whoa! That doesn’t look like a number. Try again.")
    
    print(f"🎉 Woohoo! You guessed it right! The number was {random_num}.")

guess(10)

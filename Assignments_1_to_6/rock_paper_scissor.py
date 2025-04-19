import random

def play():
    options = ['rock', 'paper', 'scissors']
    user = input("Choose rock, paper, or scissors: ").lower()
    computer = random.choice(options)

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie! 😐"
    
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'paper' and computer == 'rock') or \
       (user == 'scissors' and computer == 'paper'):
        return "You win! 🎉"

    return "You lose! 😢"

print(play())

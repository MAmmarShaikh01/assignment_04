import random

def cop_guess(x):
    low = 1
    high = x
    feedback = ''

    print(f"Think of a number between 1 and {x}, and I'll try to guess it!")

    while feedback != 'c':
        if low > high:
            print("Hmm... something's not adding up. Are you sure you responded correctly? 🤔")
            break
        
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Please respond with 'h', 'l', or 'c' only!")

    if feedback == 'c':
        print(f"Yay! I guessed your number {guess} correctly! 😎")

cop_guess(10)

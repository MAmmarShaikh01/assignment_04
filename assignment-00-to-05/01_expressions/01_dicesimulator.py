import random

def roll_pair():

    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    combined = roll_1 + roll_2
    print(f"Rolled: {roll_1} + {roll_2} = {combined}")

def main():
    roll_1 = 5505
    print(f"roll_1 in main function is {roll_1}")
    
    for i in range(3):
        print(f"\nRolling dice attempt {i + 1}:")
        roll_pair()

if __name__ == '__main__':
    main()
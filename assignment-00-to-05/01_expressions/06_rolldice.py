import random

def main():
    print("Rolling two dice...")

    def roll_dice():
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print(f"{die1} + {die2} = {total}")
    
    roll_dice()
    roll_dice()

if __name__ == '__main__':
    main()

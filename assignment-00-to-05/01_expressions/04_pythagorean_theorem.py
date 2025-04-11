import math

def main():
    
    ab = float(input("Enter the length of AB: "))
    bc = float(input("Enter the length of BC: "))

    ac = math.sqrt(ab**2 + bc**2)

    print(f"\nThe length of AC (the hypotenuse) is: {ac}")

if __name__ == '__main__':
    main()

def main():
    
    feet = float(input("Enter a length in feet: "))

    inches = feet * 12

    foot_label = "foot" if feet == 1 else "feet"
    inch_label = "inch" if inches == 1 else "inches"


    print(f"\n{feet} {foot_label} is equal to {inches} {inch_label}.")

if __name__ == '__main__':
    main()

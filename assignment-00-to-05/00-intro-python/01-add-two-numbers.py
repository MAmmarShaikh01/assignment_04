def main():
    
    fNumber = input("Please enter the first number: ")
    try:
        fNumber = int(fNumber)
    except ValueError:
        print(f" {fNumber} doesn't seem to be a valid integer. Please try again.")
        return
    
    sNumber = input("Please enter the second number: ")
    try:
        sNumber = int(sNumber)
    except ValueError:
        print(f" {sNumber} That doesn't seem to be a valid integer. Please try again.")
        return

    total = fNumber + sNumber
    print(f"The sum of {fNumber} and {sNumber} is: {total}")

if __name__ == "__main__":
    main()
def main():
    
    user_input = input("Enter temperature in Fahrenheit: ")
    
    try:
        fahrenheit = float(user_input)
    except ValueError:
        print("That doesn't look like a valid number. Please try again with a valid numeric value!")
        return

    celsius = (fahrenheit - 32) * 5.0/9.0
    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == "__main__":
    main()
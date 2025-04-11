SPEED_OF_LIGHT = 299792458 

def calculate_energy(mass):
    
    return mass * (SPEED_OF_LIGHT ** 2)

def main():
    while True:
        
        user_input = input("Enter kilos of mass (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break

        try:
            mass = float(user_input)

            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {SPEED_OF_LIGHT} m/s\n")

            energy = calculate_energy(mass)
            print(f"{energy} joules of energy!\n")

        except ValueError:
            print("Please enter a valid number for mass, or 'exit' to quit.\n")

if __name__ == '__main__':
    main()

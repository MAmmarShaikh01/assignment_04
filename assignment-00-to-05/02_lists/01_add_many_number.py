def main():
    def sum_numbers(numbers):
        total = 0
        for num in numbers:
            total += num
        return total

    exit_program = False
    while not exit_program:
        try:
            user_input = input("Enter numbers separated by spaces: ")
            number_list = [float(num) for num in user_input.strip().split()]
            result = sum_numbers(number_list)
            print(f"The sum is: {result}")

            choice = input("Would you like to enter another list? (yes/no): ").lower()
            if choice == 'no':
                exit_program = True
        except ValueError:
            print("Please enter only numbers separated by spaces!")

if __name__ == '__main__':
    main()

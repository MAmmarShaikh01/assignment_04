def main():
    numbers = [1, 2, 3, 4]
    print("Original list:", numbers)

    for i in range(len(numbers)):
        numbers[i] *= 2

    print("Doubled list:", numbers)

if __name__ == '__main__':
    main()
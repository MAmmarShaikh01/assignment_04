def main():
    num = int(input("Enter a number: "))
    curr_value = num * 2

    while curr_value < 100:
        print(curr_value, end=' ')
        curr_value = curr_value * 2

    print(curr_value)

if __name__ == '__main__':
    main()

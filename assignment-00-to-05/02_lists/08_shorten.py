MAX_LENGTH = 3

def shorten(lst):

    while len(lst) > MAX_LENGTH:
        removed = lst.pop()
        print(removed)   

def main():
    data = input("Enter items separated by spaces: ").split()
    shorten(data)
    print("Resulting list:", data)

if __name__ == "__main__":
    main()

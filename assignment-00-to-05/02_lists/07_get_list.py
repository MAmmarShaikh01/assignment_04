values = []

while True:
    entry = input("Enter a value: ")
    if entry == "":
        break
    values.append(entry)

print("Here's the list:", values)
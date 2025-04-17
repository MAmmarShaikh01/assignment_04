PETURKSBOUIPO_LIMIT = 16
STANLAU_LIMIT = 25
MAYENGUA_LIMIT = 48

def main():
    age = int(input("How old are you? "))

    if age >= PETURKSBOUIPO_LIMIT:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_LIMIT}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_LIMIT}.")

    if age >= STANLAU_LIMIT:
        print(f"You can vote in Stanlau where the voting age is {STANLAU_LIMIT}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_LIMIT}.")

    if age >= MAYENGUA_LIMIT:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_LIMIT}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_LIMIT}.")

if __name__ == "__main__":
    main()

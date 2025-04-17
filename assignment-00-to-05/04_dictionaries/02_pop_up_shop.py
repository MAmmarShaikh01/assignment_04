def main():
    prices = {
        "apple": 5.0,
        "durian": 25.0,
        "jackfruit": 15.0,
        "kiwi": 8.5,
        "rambutan": 6.0,
        "mango": 10.0
    }

    total = 0.0

    for fruit in prices:
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total += prices[fruit] * quantity

    print(f"\nYour total is ${total}")

if __name__ == "__main__":
    main()

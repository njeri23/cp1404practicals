def main():
    total_price = 0

    # Input validation for number of items
    num_items = int(input("Number of items: "))
    while num_items < 0:
        print("Invalid number of items!")
        num_items = int(input("Number of items: "))

    # Get prices and calculate total
    for i in range(num_items):
        price = float(input("Price of item: "))
        total_price += price

    # Apply discount if applicable
    if total_price > 100:
        total_price *= 0.9  # Apply 10% discount

    print(f"Total price for {num_items} items is ${total_price:.2f}")


if __name__ == "__main__":
    main()
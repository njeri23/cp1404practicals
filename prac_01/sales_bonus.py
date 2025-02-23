"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * 0.10
else:
    bonus = sales * 0.15

print(f"Bonus: ${bonus:.2f}")

def calculate_bonus(sales):
    """Calculate and return the bonus based on sales amount."""
    if sales < 1000:
        return sales * 0.10
    else:
        return sales * 0.15

# Loop to repeatedly ask for sales input
while True:
    sales = float(input("Enter sales: $"))
    if sales < 0:
        break
    bonus = calculate_bonus(sales)
    print(f"Bonus: ${bonus:.2f}")

print("Goodbye!")


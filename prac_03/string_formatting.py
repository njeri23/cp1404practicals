""" Python string formatting """

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

print(f"{year} {name} for about ${cost:,.0f}!")

# Using a for loop with range (no list) and right-aligned numbers
for i in range(11):
    print(f"2 ^ {i:2} is {2 ** i:4}")

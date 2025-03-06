def main():
    number_of_months = int(input("How many months? "))

    incomes = []

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)

def print_income_report(incomes):
    cumulative_total = 0
    print("\nIncome Report")
    print("-------------")
    for month, income in enumerate(incomes, start=1):
        cumulative_total += income
        print(f"Month {month} - Income: ${income:10.2f}         Total: ${cumulative_total:10.2f}")

if __name__ == "__main__":
    main()

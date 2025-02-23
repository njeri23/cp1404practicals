"""Temperature conversion program"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    print(f"{celsius} Celsius is equal to {celsius_to_fahrenheit(celsius)} Fahrenheit.")
    print(f"{fahrenheit} Fahrenheit is equal to {fahrenheit_to_celsius(fahrenheit)} Celsius.")

main()

"""
Answer the following questions:
1. When will a ValueError occur?
   - A ValueError occurs when the user enters a non-integer value for the numerator or denominator.
     For example, entering a string like "hello" or a float like "5.5" will raise this error.

2. When will a ZeroDivisionError occur?
   - A ZeroDivisionError occurs when the user enters 0 as the denominator,
     because division by zero is mathematically undefined.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, we can add a loop to repeatedly ask for input until the user provides a valid denominator that is not zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:  # Ensuring denominator is not zero
        print("Denominator cannot be zero. Please enter a valid number.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

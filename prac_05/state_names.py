"""
CP1404/CP5632 Practical
State names in a dictionary
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# Display all states in a neat format
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} - {name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    else:
        print("Invalid short state. Please enter a valid state code.")
    state_code = input("Enter short state: ").upper()

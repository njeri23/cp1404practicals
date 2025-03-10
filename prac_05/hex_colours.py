# Dictionary of color names and their corresponding hex codes
COLOR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

# Print available color names
print("Available colors:", ", ".join(COLOR_TO_HEX.keys()))

# Ask user for a color name and display the hex code
color_name = input("Enter a color name (or blank to quit): ")
while color_name != "":
    if color_name in COLOR_TO_HEX:
        print(f"The hex code for {color_name} is {COLOR_TO_HEX[color_name]}")
    else:
        print("Invalid color name. Try again.")
    color_name = input("Enter another color name (or blank to quit): ")

print("Goodbye!")


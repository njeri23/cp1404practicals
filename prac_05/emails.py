email_dict = {}

while True:
    email = input("Enter an email address (or press Enter to finish): ")

    if email == "":
        break

    try:
        name_part = email.split('@')[0]  # Get the part before '@'
        name = name_part.replace('.', ' ').title()  # Replace dots with spaces and capitalize the name
    except IndexError:
        print("Invalid email format. Try again.")
        continue

    confirmation = input(f"Is the name '{name}' correct? (yes/no): ").strip().lower()
    if confirmation == "yes":
        email_dict[email] = name
    else:
        print("Please try entering the email again.")

print("\nStored Emails and Names:")
for email, name in email_dict.items():
    print(f"{name:20} : {email}")

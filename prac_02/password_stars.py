""" Password Length Check """

MIN_PASSWORD_LENGTH = 8

def main():
    password = get_password()
    print_password_as_stars(password)

def get_password():
    password = input("Enter your password: ")

    while len(password) < MIN_PASSWORD_LENGTH:
        print(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long.")
        password = input("Enter your password: ")

    return password

def print_password_as_stars(password):
    print("*" * len(password))

main()


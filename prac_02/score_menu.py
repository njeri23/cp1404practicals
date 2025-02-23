""" score menu program"""

import random

def main():
    print("Welcome to the Score Menu!")
    score = int(input("Enter your score (0-100): "))

    while True:
        print("\nMenu:")
        print("(G)et a new score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Choose an option: ").upper()

        if choice == 'G':
            score = int(input("Enter a new score (0-100): "))
        elif choice == 'P':
            print(f"Result: {'Excellent' if score >= 85 else 'Passable' if score >= 50 else 'Bad'}")
        elif choice == 'S':
            print('*' * score)
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

main()

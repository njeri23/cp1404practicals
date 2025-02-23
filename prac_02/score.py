"""score result program"""

import random

def main():
    score = int(input("Enter your score: "))
    if score >= 85:
        print("Your result: Excellent")
    elif score >= 50:
        print("Your result: Passable")
    else:
        print("Your result: Bad")

    # Random score
    random_score = random.randint(0, 100)
    print(f"Random score result: {'Excellent' if random_score >= 85 else 'Passable' if random_score >= 50 else 'Bad'}")

main()

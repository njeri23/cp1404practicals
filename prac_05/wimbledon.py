FILENAME = "wimbledon.csv"


def read_wimbledon_data(filename):
    champions = {}
    champion_countries = set()

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header row
        for line in in_file:
            year, champion_country, champion, runner_up_country, runner_up, score = line.strip().split(",", maxsplit=5)
            champions[champion] = champions.get(champion, 0) + 1
            champion_countries.add(champion_country)

    return champions, champion_countries


def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, count in sorted(champions.items()):
        print(f"{champion} {count}")


def display_countries(champion_countries):
    print(f"\nThese {len(champion_countries)} countries have won Wimbledon:")
    print(", ".join(sorted(champion_countries)))


def main():
    champions, champion_countries = read_wimbledon_data(FILENAME)
    display_champions(champions)
    display_countries(champion_countries)


if __name__ == "__main__":
    main()

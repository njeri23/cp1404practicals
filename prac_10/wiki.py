"""
Wikipedia API demo
"""

import wikipedia


def main():
    print("Welcome to the Wikipedia Searcher!")
    while True:
        search_term = input("Enter a page title (or blank to quit): ").strip()
        if not search_term:
            break

        try:
            page = wikipedia.page(search_term)
            print(f"\nTitle: {page.title}")
            print(f"Summary: {wikipedia.summary(search_term, sentences=2)}")
            print(f"URL: {page.url}\n")
        except wikipedia.DisambiguationError as e:
            print(f"DisambiguationError: {search_term} may refer to multiple pages. Suggestions include:")
            print(", ".join(e.options[:5]))  # Just show a few options to avoid clutter
        except wikipedia.PageError:
            print(f"PageError: The page '{search_term}' does not exist.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

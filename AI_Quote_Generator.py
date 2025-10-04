import requests
import json
import random
from datetime import datetime

API_URL = "https://zenquotes.io/api/random"
FAVORITES_FILE = "favorite_quotes.txt"

def get_quotes():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()  # returns a list with 1 item
    except requests.RequestException as e:
        print(f"Error fetching quotes: {e}")
        return []

def display_random_quote(quotes):
    if not quotes:
        print("No quotes to display.")
        return {"text": "", "author": ""}
    quote = quotes[0]  # ZenQuotes gives one at a time
    text = quote["q"]
    author = quote["a"] if quote["a"] else "Unknown"
    print("\n💡 Quote of the Moment 💡")
    print("-" * 50)
    print(f"“{text}”")
    print(f"— {author}")
    print("-" * 50)
    return {"text": text, "author": author}

def save_favorite(quote):
    with open(FAVORITES_FILE, "a") as f:
        f.write(json.dumps(quote) + "\n")
def view_favorites():
    try:
        with open(FAVORITES_FILE, "r") as f:
            lines = f.readlines()
            if not lines:
                print("\n No favorites saved yet!")
                return
            print("\n Your Favorite Quotes:")
            print("=" * 50)
            for i, line in enumerate(lines, 1):
                q = json.loads(line)
                print(f"{i}. “{q['text']}” — {q['author']}")
            print("=" * 50)
    except FileNotFoundError:
        print("\n No favorites file found yet!")

def main():
    quotes = get_quotes()
    if not quotes:
        print("No quotes available. Please check your internet connection or try again later.")
        return

    while True:
        print("\n=== AI Quote Generator ===")
        print("1 Get a new random quote")
        print("2 View saved favorites")
        print("3 Exit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            chosen_quote = display_random_quote(quotes)
            save_choice = input("\n Save this quote? (y/n): ").strip().lower()
            if save_choice == "y":
                save_favorite(chosen_quote)
                print(" Saved to favorites!")
            print("\n", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == "2":
            view_favorites()

        elif choice == "3":
            print("\n Thanks for using the AI Quote Generator!")
            break

        else:
            print(" Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
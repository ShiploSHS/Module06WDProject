import json
import os

def restore_all_books(all_books):
    try:
        if os.path.exists("all_books.json"):
            with open("all_books.json", "r") as fp:
                all_books = json.load(fp)
        else:
            with open("all_books.json", "w") as fp:
                json.dump([], fp, indent=4)
            print("No books found, starting with an empty library.")
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading or writing file: {e}")
        all_books = []  # Start with an empty list if an error occurs
    return all_books

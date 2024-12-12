# def save_all_books(all_books):
#     with open("all_books.csv", "w") as fp:
#         for book in all_books:
#             line = f"{book['title']}, {book['author']}, {book['year']}, {book['price']}, {book['quantity']}\n"
#             fp.write(line)

import json


def save_all_books(all_books):
    try:
        with open("all_books.json", "w") as fp:
            json.dump(all_books, fp, indent=4)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error saving to file: {e}")

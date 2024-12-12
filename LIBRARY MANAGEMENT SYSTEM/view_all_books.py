# def view_all_books(all_books):
#     if all_books:
#         for book in all_books:
#             print(
#                 f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']}")
#     else:
#         print("\nNo Book found in program!")

import json

def view_all_books(all_books):
    try:
        with open("all_books.json", "r") as fp:
            all_books = json.load(fp)  # Correct function to parse the file
        if all_books:
            for book in all_books:
                print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book Added At: {book['bookAddedAt']} | Book Last Updated At: {book['bookLastUpdatedAt']}")
        else:
            print("\nNo Book found in program!")
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading file: {e}")

    if all_books:
        for book in all_books:
                print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book Added At: {book['bookAddedAt']} | Book Last Updated At: {book['bookLastUpdatedAt']}")
    else:
        print("\nNo Book found in program!")

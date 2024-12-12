import random
from datetime import datetime

import save_all_books


def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    while True:
        try:
            year = int(input("Enter Publishing Year: "))
            if year <= 0:
                print("Year must be a positive number!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid year (integer).")

    while True:
        try:
            price = float(input("Enter Book Price: "))
            if price <= 0:
                print("Price must be a positive number!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid price.")

    while True:
        try:
            quantity = int(input("Enter number of Quantity: "))
            if quantity <= 0:
                print("Quantity must be a positive integer!")
                continue
            break
        except ValueError:
            print("Invalid input! Must be a positive integer.")

    isbn = random.randint(10000, 99999)
    bookAddedAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
        "bookAddedAt": bookAddedAt,
        "bookLastUpdatedAt": bookAddedAt
    }

    all_books.append(book)
    save_all_books.save_all_books(all_books)

    print("Book Added Successfully")

    return all_books

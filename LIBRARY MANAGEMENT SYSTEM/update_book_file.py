import save_all_books
from datetime import datetime


def update_books(all_books):
    search_book = input("Enter Book Title to Update: ")

    for book in all_books:
        if book['title'] == search_book:
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
                    print("Invalid input! Please enter a valid year.")

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

            book_last_updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book['title'] = title
            book['author'] = author
            book['year'] = year
            book['price'] = price
            book['quantity'] = quantity
            book['bookLastUpdatedAt'] = book_last_updated_at

            save_all_books.save_all_books(all_books)
            print("Book Updated Successfully")
            return all_books

    print("Book Not Found!")

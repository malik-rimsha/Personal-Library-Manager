import os
import json

# File name to save the library
data_file = "library.json"

# Load library from a file
def load_library():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []

# Save library to a file
def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("Book added successfully!\n")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!\n")
            return
    print("Book not found.\n")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")

    if choice == "1":
        search_term = input("Enter the title: ").lower()
        results = [book for book in library if search_term in book["title"].lower()]
    elif choice == "2":
        search_term = input("Enter the author: ").lower()
        results = [book for book in library if search_term in book["author"].lower()]
    else:
        print("Invalid choice.\n")
        return

    if results:
        print("Matching Books:")
        for book in results:
            read_status = "Read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.\n")

# Display all books
def display_books(library):
    if not library:
        print("Your library is empty.\n")
        return

    print("Your Library:")
    for book in library:
        read_status = "Read" if book["read"] else "Unread"
        print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    print()

# Display statistics
def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book["read"]])

    if total_books == 0:
        print("No books in your library to calculate statistics.\n")
        return

    read_percentage = (read_books / total_books) * 100
    print(f"Total books: {total_books}")
    print(f"Percentage read: {read_percentage:.2f}%\n")

# Main menu
def main():
    library = load_library()

    while True:
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

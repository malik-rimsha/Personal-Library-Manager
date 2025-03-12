import streamlit as st
import json
import os

# File to store library data
FILE_NAME = "library.json"

# Load data
def load_library():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save data
def save_library(library):
    with open(FILE_NAME, "w") as f:
        json.dump(library, f)

# Initialize library
library = load_library()

st.title("📚 Personal Library Manager")

menu = st.sidebar.selectbox("Menu", ["Add Book", "Remove Book", "Search Book", "Display All Books", "Statistics"])

if menu == "Add Book":
    st.subheader("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, max_value=9999, step=1)
    genre = st.text_input("Genre")
    read_status = st.selectbox("Read Status", [True, False], format_func=lambda x: "Read" if x else "Unread")

    if st.button("Add Book"):
        library.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})
        save_library(library)
        st.success(f"Book '{title}' added successfully!")
        

elif menu == "Remove Book":
    st.subheader("Remove a Book")
    book_titles = [book["title"] for book in library]
    book_to_remove = st.selectbox("Select a book to remove", book_titles)

    if st.button("Remove Book"):
        library = [book for book in library if book["title"] != book_to_remove]
        save_library(library)
        st.success(f"Book '{book_to_remove}' removed successfully!")

elif menu == "Search Book":
    st.subheader("Search for a Book")
    search_by = st.radio("Search by", ["Title", "Author"])
    query = st.text_input(f"Enter {search_by.lower()}")

    if st.button("Search"):
        results = [book for book in library if query.lower() in book[search_by.lower()].lower()]
        if results:
            st.write(results)
        else:
            st.warning("No matching books found.")

elif menu == "Display All Books":
    st.subheader("All Books in Your Library")
    if library:
        st.table(library)
    else:
        st.warning("No books in your library.")

elif menu == "Statistics":
    st.subheader("Library Statistics")
    total_books = len(library)
    read_books = sum(book["read_status"] for book in library)
    if total_books > 0:
        st.write(f"Total Books: {total_books}")
        st.write(f"Percentage Read: {read_books / total_books * 100:.2f}%")
    else:
        st.warning("No books in your library.")

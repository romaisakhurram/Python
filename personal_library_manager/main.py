import json
import streamlit as st

st.title("Personal Library Manager")

class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials."""

    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from a JSON file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user."""
        st.subheader("Add a New Book")
        book_title = st.text_input("Enter book title:")
        book_author = st.text_input("Enter author:")
        publication_year = st.text_input("Enter publication year:")
        book_genre = st.text_input("Enter genre:")
        is_book_read = st.checkbox("Have you read this book?")

        if st.button("Add Book"):
            new_book = {
                "title": book_title,
                "author": book_author,
                "year": publication_year,
                "genre": book_genre,
                "read": is_book_read,
            }
            self.book_list.append(new_book)
            self.save_to_file()
            st.success("Book added successfully!")

    def delete_book(self):
        """Remove a book from the collection using its title."""
        st.subheader("Remove a Book")
        book_title = st.text_input("Enter the title of the book to remove:")

        if st.button("Remove Book"):
            for book in self.book_list:
                if book["title"].lower() == book_title.lower():
                    self.book_list.remove(book)
                    self.save_to_file()
                    st.success("Book removed successfully!")
                    return
            st.error("Book not found!")

    def find_book(self):
        """Search for books in the collection by title or author name."""
        st.subheader("Search for Books")
        search_type = st.radio("Search by:", ["Title", "Author"])
        search_text = st.text_input("Enter search term:")

        if st.button("Search"):
            found_books = [
                book
                for book in self.book_list
                if search_text.lower() in book["title"].lower()
                or search_text.lower() in book["author"].lower()
            ]

            if found_books:
                st.write("Matching Books:")
                for index, book in enumerate(found_books, 1):
                    reading_status = "Read" if book["read"] else "Unread"
                    st.write(
                        f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
                    )
            else:
                st.error("No matching books found.")

    def update_book(self):
        """Modify the details of an existing book in the collection."""
        st.subheader("Update Book Details")
        book_title = st.text_input("Enter the title of the book you want to edit:")

        if st.button("Find Book"):
            for book in self.book_list:
                if book["title"].lower() == book_title.lower():
                    st.write("Leave blank to keep existing value.")
                    new_title = st.text_input(f"New title ({book['title']}):", book['title'])
                    new_author = st.text_input(f"New author ({book['author']}):", book['author'])
                    new_year = st.text_input(f"New year ({book['year']}):", book['year'])
                    new_genre = st.text_input(f"New genre ({book['genre']}):", book['genre'])
                    new_read = st.checkbox("Have you read this book?", book['read'])

                    if st.button("Update Book"):
                        book["title"] = new_title or book["title"]
                        book["author"] = new_author or book["author"]
                        book["year"] = new_year or book["year"]
                        book["genre"] = new_genre or book["genre"]
                        book["read"] = new_read
                        self.save_to_file()
                        st.success("Book updated successfully!")
                        return
            st.error("Book not found!")

    def show_all_books(self):
        """Display all books in the collection with their details."""
        st.subheader("Your Book Collection")
        if not self.book_list:
            st.info("Your collection is empty.")
            return

        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            st.write(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
            )

    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        st.subheader("Reading Progress")
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0
        st.write(f"Total books in collection: {total_books}")
        st.write(f"Reading progress: {completion_rate:.2f}%")

    def start_application(self):
        """Run the main application loop with a user-friendly menu interface."""
        st.sidebar.title("Menu")
        menu_options = ["Add a new book", "Remove a book", "Search for books", "Update book details", "View all books", "View reading progress"]
        choice = st.sidebar.selectbox("Choose an option", menu_options)

        if choice == "Add a new book":
            self.create_new_book()
        elif choice == "Remove a book":
            self.delete_book()
        elif choice == "Search for books":
            self.find_book()
        elif choice == "Update book details":
            self.update_book()
        elif choice == "View all books":
            self.show_all_books()
        elif choice == "View reading progress":
            self.show_reading_progress()

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()
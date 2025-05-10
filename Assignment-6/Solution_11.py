        
class Books:
    total_books = 0

    @classmethod
    def increment_book_count(self):
        self.total_books += 1
        print(f"Total books: {self.total_books}")

book = Books()
book.increment_book_count()
book.increment_book_count()
book.increment_book_count()
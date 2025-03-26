class Building:
    def __init__(self, address, floors, year_built):
        self.address = address
        self.floors = floors
        self.__year_built = year_built

    def display_info(self):
        print(f"Address: {self.address}")
        print(f"Floors: {self.floors}")
        print(f"Year Built: {self.__year_built}")

    def renovate(self, year):
        if self.__year_built >= year:
            print("Ei saa renoveerida hoonet")
        else:
            self.__year_built = year
            self.isRenovated = True
            print(f"Building renovated to {self.__year_built}.")


class Library(Building):
    def __init__(self, address, floors, year_built, books_count):
        super().__init__(address, floors, year_built)
        self.books_count = books_count
        self.books = []  

    def display_info(self):
        super().display_info()
        print(f"Books Count: {self.books_count}")

    def list_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books in the library.")

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            self.books_count -= 1
            print(f"You have borrowed the book: {book_name}")
        else:
            print(f"Sorry, the book '{book_name}' is not available in the library.")

    def return_book(self, book_name):
        self.books.append(book_name)
        self.books_count += 1
        print(f"You have returned the book: {book_name}")

    def add_book(self, book_name):
        self.books.append(book_name)
        self.books_count += 1
        print(f"The book '{book_name}' has been added to the library.")


library = Library("Raamatukogu 1", 3, 1990, 50000)
library.display_info()


library.add_book("The Great Gatsby")
library.add_book("1984")
library.add_book("To Kill a Mockingbird")


library.list_books()


library.borrow_book("1984")
library.list_books()


library.return_book("1984")
library.list_books()

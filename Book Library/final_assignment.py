class Library:
    book_list = []
    
    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)
    
    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"Book '{self.__title}' has been borrowed.")
        else:
            raise ValueError(f"Book '{self.__title}' is already borrowed.")
        
    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"Book '{self.__title}' has been returned.")
        else:
            raise ValueError(f"Book '{self.__title}' is not borrowed and  available.")
        
    def view_book_info(self):
        is_available = "Available" if self.__availability else "Not Available"
        print(f"Book ID: {self.__book_id}, Title: '{self.__title}', Author: {self.__author}, Availability: {is_available}")

def menu():
    while True:
        print("-----------------")
        print("1. View all books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        print("-----------------")

        try:
            select = int(input('Select an option: '))
            if select == 1:
                print("All Books:")
                for book in Library.book_list:
                    book.view_book_info()
            elif select == 2:
                book_id = int(input("Enter Book ID: "))
                found = False
                for book in Library.book_list:
                    if book._Book__book_id == book_id: 
                        found = True
                        try:
                            book.borrow_book()
                        except ValueError as s:
                            print(s)
                        break
                if not found:
                    print(f"No book found with ID {book_id}.")
            elif select == 3:
                book_id = int(input("Enter Book ID: "))
                found = False
                for book in Library.book_list:
                    if book._Book__book_id == book_id:  
                        found = True
                        try:
                            book.return_book()
                        except ValueError as s:
                            print(s)
                        break
                if not found:
                    print(f"No book found with ID {book_id}.")
            elif select == 4:
                print("Exiting...")
                break
            else:
                print("Invalid option. Please select a valid number.")
        except ValueError as s:
            print(f"Error: {s}. Please enter a valid number.")

book1 = Book(101,'Time Managment','Brian Tracy')
book2 = Book(102,'Eat That Frog','Habibur Rahman')
book3 = Book(103,'Ontim Muhurto','Abdullah yusuf')


menu()

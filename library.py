from finalProject.book import Book
from finalProject.customer import Customer

class Library:
    """ Abstract base class for library object

    Attributes:
        name (string): name of the library
        location (string): address of the library
        books (list of Book): all the books carried by the library
        customers (Dict customer name: rest of customer info): all the customers who checked out a book and the rest of their info
    """

    def __init__(self, name, location):
        """ Initializes new Library object

        Side Effect:
            Sets attribute name, location, books, and customers
        """

        self.name = name
        self.location = location
        self.books = []
        self.customers = {}

    def add_book(self, book):
        """ Adds a book to the library

        Args:
            book (Book): Book object to add to library
        
        Side effects:
            Adds book to books list
        """

        self.books.append(book)

    def add_customer(self, customer):
        """ Adds a customer to the library

        Args:
            customer (Customer): Customer to add to library
        
        Side effects:
            Adds customer as key and rest of customer info as value to customer dictionary
        """

        self.customers[customer.name] = [customer.email, customer.address, customer.phone_number]

    def checkout_book_by_title(self, book_name):
        """ Check out book by given book name

        Args:
            book_name (string): name of the book wanted to be checked out
        
        Returns:
            Returns a list of books to be checked out 

        Side effects:
            Book object gets removed from self.books
        """

        for book in self.books:
            if book.name == book_name:
                self.books.remove(book)
                return [book]

        raise ValueError("Book wasn't found")

    def checkout_book_by_genre(self, book_genre):
        """ Check out book by given book genre

        Args:
            book_genre (string): genre of the book wanted to be checked out
        
        Returns:
            Returns a list of books to be checked out 

        Side effects:
            Book object gets removed from self.books
        """

        return_list = []

        for book in self.books:
            if book.genre == book_genre:
                self.books.remove(book)
                return_list.append(book)

        if len(return_list) != 0:
            return return_list

        raise ValueError("Book wasn't found")

    def checkout_book_by_author(self, author_name):
        """ Check out book by given author_name

        Args:
            author_name (string): name of the author of book wanted to be checked out
        
        Returns:
            Returns a list of books to be checked out 

        Side effects:
            Book object gets removed from self.books
        """

        return_list = []

        for book in self.books:
            if book.author == author_name:
                self.books.remove(book)
                return_list.append(book)

        if len(return_list) != 0:
            return return_list

        raise ValueError("Book wasn't found")

    def return_books(self, customer_books):
        """ Returns the books customer has checked out back to library

        Args:
            customer_books (list of books): list of books customer has checked out
        
        Side effects:
            Appends the books from customer back to self.book list
        """

        for book in customer_books:
            self.books.append(book)

    def curr_inventory(self):
        """ Shows the library inventory of books

        Side Effect:
            Prints out self.books list
        """

        names = []

        for book in self.books:
            names.append(book.name)

        print(names)


def main():

    suraj_library = Library("Suraj's Library", "College Park, MD 20742")

    classic_books = [Book("Pride and Prejudice", 279, "Historical Fiction", "Jane Austen"),
                    Book("To Kill a Mockingbird", 336, "Fiction", "Harper Lee"), 
                    Book("The Great Gatsby", 180, "Fiction", "F. Scott Fitzgerald"), 
                    Book("The Hunger Games", 374, "Dystopia", "Suzanne Collins"),
                    Book("Life of Pi", 460, "Fantasy", "Yann Martel"), 
                    Book("The Da Vinci Code", 489, "Mystery", "Dan Brown"), 
                    Book("Harry Potter and the Goblet of Fire", 734, "Fantasy", "J.K. Rowling"),
                    Book("A Game of Thrones", 835, "Epic Fantasy", "George R.R. Martin"), 
                    Book("It", 1116, "Horror", "Stephen King"), 
                    Book("Automate the Boring Stuff with Python: Practical Programming for Total Beginners", 479, "Programming", "Al Sweigart")]
    
    for book in classic_books:
        suraj_library.add_book(book)

    suraj_library.curr_inventory()

    first_customer = Customer()
    suraj_library.add_customer(first_customer)

    print(suraj_library.customers)

    name_choice = first_customer.what_book_name()
    checked_out = suraj_library.checkout_book_by_title(name_choice)
    first_customer.borrow_book(checked_out)

    suraj_library.curr_inventory()
    first_customer.print_borrowed()

    genre_choice = first_customer.what_genre()
    checked_out = suraj_library.checkout_book_by_genre(genre_choice)
    first_customer.borrow_book(checked_out)

    suraj_library.curr_inventory()
    first_customer.print_borrowed()

    author_choice = first_customer.what_author()
    checked_out = suraj_library.checkout_book_by_author(author_choice)
    first_customer.borrow_book(checked_out)

    suraj_library.curr_inventory()
    first_customer.print_borrowed()

    suraj_library.return_books(first_customer.borrowed_books)
    first_customer.return_books()

    print("Final library inventory")
    suraj_library.curr_inventory()
    print("Final customer list")
    first_customer.print_borrowed()

if __name__ == "__main__":
    main()
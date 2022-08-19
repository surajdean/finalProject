class Customer:
    """ Abstract base class for library customer
    
    Attributes:
        name (String): name of the customer
        email (String): email address of the customer
        address (String): home address of the customer
        phone_number (String): phone number of the customer
        borrowed_books (List of Books): books checked out by the customer
    """

    def __init__(self):
        """ Initializes new Customer object

        Side Effect:
            Sets attribute name, email, address, phone_number, and borrowed_books
        """

        self.name = input("What is your name?: ")
        self.email = input("What is your email?: ")
        self.address = input("What is your address?: ")
        self.phone_number = input("What is your phone number?: ")
        self.borrowed_books = []

    def what_book_name(self):
        """ Asks the user for what book (title) the customer wants
        
        Returns:
            String: name of the book wanted by customer
        """

        return input("What book do you want (enter name/title of book)?: ")

    def what_genre(self):
        """ Asks the user for what genre of books the customer wants
        
        Returns:
            String: genre of books wanted by customer
        """

        return input("What genre do you want (enter genre)?: ")

    def what_author(self):
        """ Asks the user for what author the customer wants
        
        Returns:
            String: name of author wanted by customer
        """

        return input("What author do you want (enter author name)?: ")

    def borrow_book(self, book_list):
        """ Adds the list of books requested to borrow to customers borrowed books

        Args:
            book_list (list of Books): list of books or singular book borrowed by customer

        Side Effect:
            Appends book_list to attribute borrowed_books
        """

        self.borrowed_books.extend(book_list)

    def return_books(self):
        """ Returns all the checked out books of customer

        Side Effect:
            Clears the customer books list
        """

        self.borrowed_books.clear()

    def print_borrowed(self):
        """ Prints out all the borrowed books of the customer

        Side Effect:
            Prints all the names of books from customer's borrowed_books
        """

        names = []

        for book in self.borrowed_books:
            names.append(book.name)

        print(names)
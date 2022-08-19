class Book:
    """ Abstract base class for book object
    
    Attributes:
        name (string): title of book
        page_length (int): number of pages in book
        genre (string): genre of the book
        author (string): author who wrote the book
    """

    def __init__(self, name, page_length, genre, author):
        """ Initializes new Book object

        Side Effect:
            Sets attribute name, page_length, genre, author
        """

        self.name = name
        self.page_length = page_length
        self.genre = genre
        self.author = author
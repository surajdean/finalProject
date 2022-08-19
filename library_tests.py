from book import Book
from customer import Customer
from library import Library

def test_add_book():

	new_library = Library("Suraj's Library", "College Park, MD 20742")
	new_library.add_book(Book("Pride and Prejudice", 279, "Historical Fiction", "Jane Austen"))
	assert new_library.books == [Book("Pride and Prejudice", 279, "Historical Fiction", "Jane Austen")]
	new_library.add_book(Book("To Kill a Mockingbird", 336, "Fiction", "Harper Lee"))
	new_library.add_book(Book("The Great Gatsby", 180, "Fiction", "F. Scott Fitzgerald"))
	assert new_library.books == [Book("Pride and Prejudice", 279, "Historical Fiction", "Jane Austen"), Book("To Kill a Mockingbird", 336, "Fiction", "Harper Lee"), Book("The Great Gatsby", 180, "Fiction", "F. Scott Fitzgerald")]

def test_checkout_book_title():

	new_library = Library("Suraj's Library", "College Park, MD 20742")
	new_library.books.extend([Book("Pride and Prejudice", 279, "Historical Fiction", "Jane Austen"), Book("To Kill a Mockingbird", 336, "Fiction", "Harper Lee"), Book("The Great Gatsby", 180, "Fiction", "F. Scott Fitzgerald")])
	assert new_library.checkout_book_by_title("Pride and Prejudice") == [Book("Pride and Prejudice", 279, "Historical Fiction", "Jane Austen")]

def test_checkout_book_by_genre():

	new_library = Library("Suraj's Library", "College Park, MD 20742")
	new_library.books.extend([Book("Pride and Prejudice", 279, "Historical Fiction", "Jane Austen"), Book("To Kill a Mockingbird", 336, "Fiction", "Harper Lee"), Book("The Great Gatsby", 180, "Fiction", "F. Scott Fitzgerald")])
	assert new_library.checkout_book_by_genre("Fiction") == [Book("To Kill a Mockingbird", 336, "Fiction", "Harper Lee"), Book("The Great Gatsby", 180, "Fiction", "F. Scott Fitzgerald")]

def test_checkout_book_by_author():

	new_library = Library("Suraj's Library", "College Park, MD 20742")
	new_library.books.extend([Book("Pride and Prejudice", 279, "Historical Fiction", "Jane Austen"), Book("To Kill a Mockingbird", 336, "Fiction", "Harper Lee"), Book("The Great Gatsby", 180, "Fiction", "F. Scott Fitzgerald")])
	assert new_library.checkout_book_by_author("Jane Austen") == [Book("Pride and Prejudice", 279, "Historical Fiction", "Jane Austen")]

def test_return_books():

	new_library = Library("Suraj's Library", "College Park, MD 20742")
	book_list = [Book("Pride and Prejudice", 279, "Historical Fiction", "Jane Austen"), Book("To Kill a Mockingbird", 336, "Fiction", "Harper Lee"), Book("The Great Gatsby", 180, "Fiction", "F. Scott Fitzgerald")]
	assert new_library.return_books(book_list) == book_list

test_add_book()
test_checkout_book_title()
test_checkout_book_by_genre()
test_checkout_book_by_author()
test_return_books()
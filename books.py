from random import choice
from datetime import datetime
from titlecase import titlecase

running = True
books = []
booklist = "books.txt"
year = datetime.now().year
books_read = str(year) + " books.txt"
today = datetime.now().strftime('%m/%d')


open(booklist, 'a').close()
open(books_read, 'a').close()


with open(booklist, 'r') as bookimport:
	for book in bookimport:
		books.append(book.strip('\n').lower())


def save_book_list():
	with open(booklist, 'w') as booksave:
		for book in sorted(books):
			print(titlecase(book), file=booksave)

def add_new_book(book_title):
	if book_title in books:
		return "{} is already in your list".format(titlecase(book_title))
	else:
		books.append(book_title)
		save_book_list()
		return "{} added".format(titlecase(book))


def add_read_book(book_title):
	book_with_author = ''
	for book in books:
		if book.startswith(book_title) is True:
			book_with_author = book
			books.remove(book)
			save_book_list()
			break
	dated_title = today + ' ' + titlecase(book_with_author)
	with open(books_read, 'a') as bookwrite:
		bookwrite.write("\n" + dated_title)
	return book_with_author

def get_book_info():
	book = input("Book Title: ").lower()
	if book == '':
		return
	else:
		author = input("Author: ").lower()
		if author == '':
			new_book = book
		else:
			new_book = "{} by {}".format(book, author)
		return new_book
		

def get_book_title():
	book = input("Book Title: ")
	if book == '':
		return
	return book


def get_random_book():
	book_to_read = choice(books)
	return book_to_read


def delete_book(book_to_delete):
	book_with_author = ''
	for book in books:
		if book.startswith(book_to_delete) is True:
			book_with_author = book
	if book_with_author in books:
		books.remove(book_with_author)
		save_book_list()
		return "{} removed from list".format(titlecase(book_with_author))
	else:
		return "{} is not in your list".format(titlecase(book_to_delete))
		

running = True
while running:
	new_book = input("""
[A]dd a new book
[L]og a book as read
[R]andom book selection
[D]elete a book
[V]iew book list
[S]ee read list
[E]xit
""").lower()


	if new_book == "a":
		book = get_book_info()
		book_addition = add_new_book(book)
		print(book_addition)

	if new_book == "l":
		book = get_book_title()
		book_addition = add_read_book(book)
		print("{} logged as read".format(titlecase(book_addition)))

	if new_book == "r":
		book_to_read = get_random_book()
		print("You should read {}".format(titlecase(book_to_read)))
		
	if new_book == "d":
		deleted_book = get_book_title()
		book = delete_book(deleted_book)
		print(book)
	if new_book == "v":
		print("-" * 40)
		for book in books:
			print(titlecase(book))
		print("-" * 40)
	if new_book == "s":
		print("-" * 40)
		with open(books_read) as readlist:
			for book in readlist:
				print(book.strip("\n"))
		print("-" * 40)
	if new_book == 'e':
		break

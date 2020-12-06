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

with open(booklist, 'r') as bookimport:
	for book in bookimport:
		books.append(book.strip('\n').lower())


def save_book_list():
	books = sort_books()
	with open(booklist, 'w') as booksave:
		for title in books:
			print(titlecase(title), file=booksave)

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
	dated_title = today + ' ' + titlecase(book_with_author)
	with open(books_read, 'a') as bookwrite:
		bookwrite.write("\n" + dated_title)
	return book_with_author

def get_book_info():
	book = input("Book Title: ").lower()
	if book == '':
		return book
	else:
		author = input("Author: ").lower()
		if author == '':
			new_book = book
		else:
			new_book = "{} by {}".format(book, author)
		return new_book
		

def get_book_title():
	book = input("Book Title: ")
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


def sort_books():
	books_with_the = [title for title in books if title.startswith("the ")]
	books_with_a = [title for title in books if title.startswith("a ")]
	books_with_an = [title for title in book if title.startswith("an ")]
	books_the_cleaned = []
	books_a_cleaned = []
	books_an_cleaned = []
	for title in books_with_the:
		books_the_cleaned.append(title.replace("the ", ""))
		books.remove(title)
	for title in books_with_a:
		books_a_cleaned.append(title.replace("a ", ""))
		books.remove(title)
	for title in books_with_an:
		books_an_cleaned.append(title.replace("an ", ""))
		books.remove(title)
	for title in books_the_cleaned:
		books.append(title)
	for title in books_a_cleaned:
		books.append(title)
	for title in books_an_cleaned:
		books.append(title)
	books.sort()
	for title in books:
		if title in books_the_cleaned:
			books[books.index(title)] = books_with_the[books_the_cleaned.index(title)]
		elif title in books_a_cleaned:
			books[books.index(title)] = books_with_a[books_a_cleaned.index(title)]
		elif title in books_an_cleaned:
			books[books.index(title)] = books_with_an[books_an_cleaned.index(title)]
	return books


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
		if book != '':
			book_addition = add_new_book(book)
			print(book_addition)
	if new_book == "l":
		book = get_book_title()
		if book != '':
			book_addition = add_read_book(book)
			print("{} logged as read".format(titlecase(book_addition)))
	if new_book == "r":
		book_to_read = get_random_book()
		print("You should read {}".format(titlecase(book_to_read)))
	if new_book == "d":
		deleted_book = get_book_title()
		if deleted_book != "":
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

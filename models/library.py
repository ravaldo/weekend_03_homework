from models.book import Book


class Library():
	def __init__(self, name, address, books=None):
		if books is None: books = []
		self.name = name
		self.address = address
		self.books = books

	def add_book(self, book):
		self.books.append(book)

	def remove_book(self, book):
		if book in self.books:
			self.books.remove(book)

	def remove_book_by_index(self, i):
		self.books.pop(i)

	def find_books_by_author(self, name):
		return [b for b in self.books if name in b.author]

	def find_books_by_genre(self, genre):
		return [b for b in self.books if genre in b.genre]



book1 = Book("Romeo and Juliet", "William Shakespeare", ["classic", "plays"], 281, True)
book2 = Book("Macbeth", "William Shakespeare", ["classic", "plays"], 249)
book3 = Book("Hamlet", "William Shakespeare", ["classic", "plays"], 289, True)
book4 = Book("Nineteen Eighty-Four", "George Orwell", ["classic", "science fiction"], 355)
book5 = Book("The Catcher in the Rye", "J.D. Salinger", ["literature", "fiction", "coming of age"], 277)

library = Library("The Library of Classics", "Glasgow")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)


#if __name__ == "__main__":	
#	for b in library.books:
#		print(b)
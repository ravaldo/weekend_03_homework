import unittest
from models.library import Library
from models.book import Book

class TestLibrary(unittest.TestCase):
	
	def setUp(self):
		self.book1 = Book("Romeo and Juliet", "William Shakespeare", ["classic", "plays"], 281, True)
		self.book2 = Book("Macbeth", "William Shakespeare", ["classic", "plays"], 249)
		self.book3 = Book("Hamlet", "William Shakespeare", ["classic", "plays"], 289, True)
		self.book4 = Book("Nineteen Eighty-Four", "George Orwell", ["classic", "science fiction"], 355)
		self.book5 = Book("The Catcher in the Rye", "J.D. Salinger", ["literature", "fiction", "coming of age"], 277)
		
		self.library = Library("The Library of Classics", "Glasgow")
		self.library.add_book(self.book1)
		self.library.add_book(self.book2)
		self.library.add_book(self.book3)
		self.library.add_book(self.book4)
	
	def test_add_book(self):
		self.assertEqual(len(self.library.books), 4)
		self.library.add_book(self.book5)
		self.assertEqual(len(self.library.books), 5)
		self.assertEqual(self.library.books[4].title, "The Catcher in the Rye")
	
	def test_remove_book(self):
		self.assertEqual(len(self.library.books), 4)
		self.library.remove_book(self.book5)			# not in the catalog
		self.assertEqual(len(self.library.books), 4)	# nothing should have changed
		self.library.remove_book(self.book4)			
		self.assertEqual(len(self.library.books), 3)
	
	def test_find_books_by_author(self):
		results = len(self.library.find_books_by_author("Shakespeare"))
		self.assertEqual(results, 3)
		results = len(self.library.find_books_by_author("Hemmingway"))
		self.assertEqual(results, 0)
	
	def test_find_books_by_genre(self):
		results = len(self.library.find_books_by_genre("plays"))
		self.assertEqual(results, 3)
		results = len(self.library.find_books_by_genre("science fiction"))
		self.assertEqual(results, 1)
		

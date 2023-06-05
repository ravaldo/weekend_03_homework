import unittest
from models.book import Book


class TestBook(unittest.TestCase):
	
	def setUp(self):
		self.book = Book("Romeo and Juliet", "William Shakespeare", ["classic", "plays"], 281, True)
	
	def test_title(self):
		self.assertEqual(self.book.title, "Romeo and Juliet")
	
	def test_author(self):
		self.assertEqual(self.book.author, "William Shakespeare")
	
	def test_genre(self):
		self.assertEqual(len(self.book.genre), 2)
		self.assertEqual(True, "classic" in self.book.genre)
		self.assertEqual(True, "plays" in self.book.genre)
	
	def test_pages(self):
		self.assertEqual(self.book.numpages, 281)
	
	def test_availability(self):
		self.assertEqual(self.book.is_available(), False)
		self.assertEqual(self.book.checkedout, True)
		
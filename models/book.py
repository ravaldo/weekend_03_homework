

class Book():
	def __init__(self, title, author, genre, numpages, checkedout=False):
		self.title = title
		self.author = author
		self.genre = genre
		self.numpages = numpages
		self.checkedout = checkedout
		
	def is_available(self):
		return not self.checkedout
	
	def __repr__(self):
		return f"{self.title} by {self.author}"
		
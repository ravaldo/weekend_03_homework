from flask import render_template, redirect, request
from app import app

from models.book import Book
from models.library import Library, library


@app.route('/')
def root():
	return redirect('/books')


@app.route('/books')
def show_books():
	return render_template('index.html', title=library.name, books=library.books)


@app.route('/books/<index>')
def show_book(index):
	book = library.books[int(index)]
	return render_template('book_detail.html', title=library.name, book=book)


@app.route('/books/<index>', methods=['post'])
def book_admin(index):
#	print(request.form)
	if request.form["book-admin"] == "checked_in":
		library.books[int(index)].checkedout = False
		return redirect(request.url)
	if request.form["book-admin"] == "checked_out":
		library.books[int(index)].checkedout = True
		return redirect(request.url)
	if request.form["book-admin"] == "delete":
		return redirect(f'/books/delete/{index}')

	
@app.route('/books', methods=['post'])
def add_book():
	title = request.form["title"]
	author = request.form["author"]
	genre = request.form["genre"].split(',')
	numpages = request.form["numpages"]
	book = Book(title, author, genre, numpages)
	library.add_book(book)
	return redirect('/books')


@app.route('/books/delete/<index>')
def delete_book(index):
	book = library.books[int(index)]
	library.remove_book(book)
	return redirect("/books")
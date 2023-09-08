from flask import render_template, Blueprint, request
from models.book_list import library, add_new_book
from models.book import Book

library_blueprint = Blueprint("library", __name__)

@library_blueprint.route("/library")
def index():
    return render_template("index.jinja", title="Library", library=library)

@library_blueprint.route("/library", methods=["POST"])
def add_book():
    print(request.form)
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre)
    add_new_book(new_book)
    return "Complete" #might want to add a redirect here
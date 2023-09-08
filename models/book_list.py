from models.book import Book

book1 = Book("Pride and Prejudice", "Jane Austen", "Classic")
book2 = Book("The Eyre Affair", "Jasper Fforde", "Science Fiction")
book3 = Book("Wintering", "Katherine May", "Health & Wellbeing")

library = [book1, book2, book3]

def add_new_book(new_book):
    library.append(new_book)

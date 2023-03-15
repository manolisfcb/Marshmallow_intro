from marshmallow import Schema, fields, INCLUDE, EXCLUDE

"""
INCLUDE: Include unknown fields in the deserialized result.
EXCLUDE: Exclude unknown fields from the deserialized result.

Essentially, INCLUDE and EXCLUDE are the same as RAISE_ERROR, except that they
include or exclude unknown fields from the deserialized result, respectively.

"""


class BookSchema(Schema):
    title = fields.Str()
    author = fields.Str()


#incoming_book_data from a request    
incoming_book = {
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "description": "Science fiction comedy adventure"
}

book_schema = BookSchema(unknown=EXCLUDE) # Si no se especifica, por defecto es RAISE_ERROR
book = book_schema.load(incoming_book)

print (book)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __repr__(self):
        return f"Book(title={self.title}, author={self.author})"
        
book_obj = Book(**book)

print(book_obj)
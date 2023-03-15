from marshmallow import Schema, fields

class BookSchema(Schema):
    title = fields.Str()
    author = fields.Str()
    

class Book:
    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description

book = Book(title="The Hitchhiker's Guide to the Galaxy", author="Douglas Adams", description="Science fiction comedy adventure")
print(book)

book_schema = BookSchema()
book_json = book_schema.dump(book)
print(book_json)
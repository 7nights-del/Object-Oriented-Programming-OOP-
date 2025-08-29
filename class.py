# Base class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def read(self):
        return f"Reading '{self.title}' by {self.author}."
    
    def info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

# Child class (Inheritance)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)  # call parent constructor
        self.file_size = file_size
    
    # Method overriding (polymorphism)
    def read(self):
        return f"Reading '{self.title}' by {self.author} on an e-reader"
    
    def download(self):
        return f"Downloading '{self.title}' ({self.file_size}MB)..."

# Create objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
ebook1 = EBook("Python Programming", "Guido van Rossum", 350, 5)

print(book1.info())
print(book1.read())

print(ebook1.info())
print(ebook1.read())     
print(ebook1.download())
